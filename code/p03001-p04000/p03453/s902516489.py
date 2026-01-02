import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

from heapq import *

def solve():
    dist = [inf] * n
    cnt = [0] * n
    hp = []
    heappush(hp, (0, s))
    dist[s] = 0
    cnt[s] = 1
    while hp:
        d, u = heappop(hp)
        if d > dist[t]: break
        if d > dist[u]: continue
        for v, c in to[u]:
            nd = d + c
            if nd == dist[v]: cnt[v] += cnt[u]
            elif nd < dist[v]:
                dist[v] = nd
                cnt[v] = cnt[u]
                heappush(hp, (nd, v))

    distr = [inf] * n
    cntr = [0] * n
    hp = []
    heappush(hp, (0, t))
    distr[t] = 0
    cntr[t] = 1
    while hp:
        d, u = heappop(hp)
        #print(d,u,hp,distr,cntr)
        if d * 2 > dist[t]: continue
        if d > distr[u]: continue
        for v, c in to[u]:
            nd = d + c
            if nd == distr[v]: cntr[v] += cntr[u]
            elif nd < distr[v]:
                distr[v] = nd
                cntr[v] = cntr[u]
                heappush(hp, (nd, v))

    ans = pow(cnt[t], 2, md)
    dt = dist[t]
    for u in range(n):
        if dist[u] * 2 == dt:
            ans -= (cnt[u] * cntr[u])**2
            ans %= md
    for u, v, c in uvd:
        for _ in range(2):
            if dist[u] + distr[v] + c == dt and dist[u] * 2 < dt and distr[v] * 2 < dt:
                ans -= (cnt[u] * cntr[v])**2
                ans %= md
            u, v = v, u
    print(ans)

md = 10 ** 9 + 7
inf = 10 ** 16
n, m = MI()
s, t = MI1()
to = [[] for _ in range(n)]
uvd = []
for _ in range(m):
    u, v, d = MI()
    to[u - 1].append((v - 1, d))
    to[v - 1].append((u - 1, d))
    uvd.append((u - 1, v - 1, d))

solve()
