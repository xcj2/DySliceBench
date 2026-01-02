import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def root(par, x):
    if par[x] == x:
        return x
    else:
        return root(par, par[x])


def unite(rank, par, x, y):
    x = root(par, x)
    y = root(par, y)

    if x == y:
        par[x] = y

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def main():
    N, M = map(int, readline().split())
    p = list(map(int, readline().split()))
    m = map(int, read().split())
    XY = list(zip(m, m))

    par = list(range(N))
    rank = [0] * N

    for x, y in XY:
        x -= 1
        y -= 1
        unite(rank, par, x, y)

    d_p = defaultdict(list)
    d_index = defaultdict(list)
    for i in range(N):
        par[i] = root(par, i)
        d_index[par[i]].append(p[i])
        d_p[par[i]].append(i+1)

    cnt = 0
    for i in set(par):
        cnt += len(list(set(d_index[i]) & set(d_p[i])))

    print(cnt)


main()
