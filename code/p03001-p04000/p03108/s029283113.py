import sys
sys.setrecursionlimit(1000000)

def get_root(s):
    if s != root[s]:
        root[s] = get_root(root[s])
        return root[s]
    return s

def unite(s, t):
    root_s = get_root(s)
    root_t = get_root(t)
    if not root_s == root_t:
        if rank[s] == rank[t]:
            root[root_t] = root_s
            rank[root_s] += 1
        elif rank[s] > rank[t]:
            root[root_t] = root_s
        else:
            root[root_s] = root_t

def same(s, t):
    if get_root(s) == get_root(t):
        return True
    else:
        return False

def get_size(s):
    return size[get_root(s)]

def update_size(x, y, s):
    size[get_root(s)] = x + y

n, m = map(int, input().split())
c = (n * (n - 1)) // 2
root = [i for i in range(n)]
rank = [1 for _ in range(n)]
size = [1 for _ in range(n)]
ans = [c]
v = [list(map(int, input().split())) for _ in range(m)]
for i in range(m - 1, -1, -1):
    u = v[i]
    u[0] -= 1
    u[1] -= 1
    if not same(u[0], u[1]):
        x = get_size(u[0])
        y = get_size(u[1])
        unite(u[0], u[1])
        update_size(x, y, u[0])
        c -= x * y
    ans.append(c)
for i in range(m - 1, -1, -1):
    print(ans[i])