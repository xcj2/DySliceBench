from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

root = None
def insert(z):
    global root
    y = None
    x = root
    while x:
        y = x
        x = x[z[2] >= x[2]]
    z[3] = y

    if not y:
        root = z
    else:
        y.__setitem__(z[2] >= y[2], z)

def find(k):
    x = root
    while x:
        if x[2] == k:
            return 1
        x = x[k >= x[2]]
    return 0

def __delete(x):
    global root
    if x[0] and x[1]:
        y = x[1]
        while y[0]:
            y = y[0]
        x[2] = y[2]
        __delete(y)
    elif not x[0] and not x[1]:
        if x[3]:
            p = x[3]
            p.__setitem__(p[1] is x, None)
        else:
            root = None
        del x
    else:
        y = x[0] or x[1]

        if x[3]:
            p = x[3]

            y[3] = p
            p[p[1] is x] = y
        else:
            y[3] = None
            root = y
        del x

def delete(k):
    x = root
    while x:
        if x[2] == k:
            break
        x = x[k >= x[2]]
    if not x:
        return
    __delete(x)

def debug():
    s0 = [""]
    s1 = [""]

    def dfs(nd):
        v = str(nd[2])
        s0.append(v)
        if nd[0]:
            dfs(nd[0])
        s1.append(v)
        if nd[1]:
            dfs(nd[1])
    dfs(root)
    return " ".join(s1), " ".join(s0)


M = int(readline())
ans = []
for m in range(M):
    cmd, *V, = readline().split()
    if cmd == "print":
        ans.extend(debug())
    elif cmd == "find":
        ans.append("yes" if find(int(V[0])) else "no")
    elif cmd == "delete":
        delete(int(V[0]))
    else:
        insert([None, None, int(V[0]), None])
write("\n".join(ans))
write("\n")

