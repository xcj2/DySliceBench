from collections import defaultdict
import sys

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
        return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def main():
    N, K, L = map(int, readline().split())
    m = map(int, read().split())
    pq = list(zip(m, m))
    pq, rs = pq[:K], pq[K:]

    par = list(range(N))
    rank = [0] * N
    for p, q in pq:
        p -= 1
        q -= 1
        unite(rank, par, p, q)

    par_t = list(range(N))
    rank_t = [0] * N
    for r, s in rs:
        r -= 1
        s -= 1
        unite(rank_t, par_t, r, s)

    pp = [(0, 0)]*N
    dd = defaultdict(list)
    for i in range(N):
        par[i] = root(par, i)
        par_t[i] = root(par_t, i)
        pp[i] = (par[i], par_t[i])
        dd[pp[i]].append(i)

    cnt = [0] * N
    for i in range(N):
        cnt[i] = len(dd[pp[i]])

    print(*cnt)


main()
