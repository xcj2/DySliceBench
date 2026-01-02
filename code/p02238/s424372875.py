from collections import deque


N = 100
WHITE = 0
GRAY = 1
BLACK = 2

M = [[0 for _ in range(N)] for _ in range(N)]
color = [0 for _ in range(N)]
d = [0 for _ in range(N)]
f = [0 for _ in range(N)]
nt = [0 for _ in range(N)]
tt = 0


def main():
    n = int(input())
    for _ in range(n):
        u, k, *v_s = map(int, input().split(' '))
        for j in range(k):
            M[u-1][v_s[j-1]-1] = 1

    dfs(n)

    for i in range(n):
        print('{} {} {}'.format(i+1, d[i], f[i]))


def dfs(n):
    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(n, u)


def dfs_visit(n, r):
    global tt
    color[r] = GRAY
    tt += 1
    d[r] = tt
    for v in range(0, n):
        if M[r][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(n, v)
    color[r] = BLACK
    tt += 1
    f[r] = tt


if __name__ == '__main__':
    main()

