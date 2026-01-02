#template
def inputlist(): return [int(j) for j in input().split()]
#template
import copy
def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)
def check(s,n):
    if len(s) < n:
        d = n-len(s)
        for _ in range(d):
            s = '0'+s
    return s
ans = 0
H,W,K = inputlist()
maze = [[0] for _ in range(H)]
for i in range(H):
    maze[i] = list(input())
maza = copy.deepcopy(maze)
for i in range(2**H):
    xi = base10to(i,2)
    xi = check(xi,H)
    x_ = []
    for ind in range(H):
        if xi[ind] == "1":
            x_.append(ind)
    for j in range(2**W):
        yj = base10to(j,2)
        yj = check(yj,W)
        y_ = []
        for stu in range(W):
            if yj[stu] == "1":
                y_.append(stu)
        for x in x_:
            maze[x] = ["x" for _ in range(W)]
        for y in y_:
            for xa in range(H):
                maze[xa][y] = "x"
        count = 0
        for a in range(H):
            for b in range(W):
                if maze[a][b] == "#":
                    count+=1
        if count == K:
            ans +=1
        maze = copy.deepcopy(maza)

print(ans)