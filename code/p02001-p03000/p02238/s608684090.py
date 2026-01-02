WHITE = 0
GRAY = 1
BLACK = 2
tt = -1

def next(u, m, n, nt):
    start = nt[u]
    for v in range(start, n):
        nt[u] = v + 1
        if m[u][v]:
            return v
    return -1


def dfs_visit(r, m, n, color, d, f):
    nt = [0] * n
    stack = [r]
    color[r] = GRAY
    global tt
    tt += 1
    d[r] = tt

    while len(stack) != 0:
        u = stack[-1]
        v = next(u, m, n, nt)
        if v != -1:
            if color[v] == WHITE:
                color[v] = GRAY
                tt += 1
                d[v] = tt
                stack.append(v)
        else:
            stack.pop()
            color[u] = BLACK
            tt += 1
            f[u] = tt


def dfs(n, m):
    color = [WHITE] * n
    d = [-1] * n
    f = [-1] * n
    global tt
    tt = 0
    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(u, m, n, color, d, f)
    for i in range(n):
        print('{0} {1} {2}'.format(i+1, d[i], f[i]))



n = int(input())
m = [[False] * n for i in range(n)]
for i in range(n):
    line = [int(v) for v in input().split()]
    u = line[0] - 1
    for v in line[2:]:
        v -= 1
        m[u][v] = True

dfs(n, m)
