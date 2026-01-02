import sys
sys.setrecursionlimit(1000000)
mod = 7 + 10 ** 9
from collections import deque

def comb(n, r, fact, revfact, mod):
    return (fact[n] * revfact[n-r] * revfact[r]) % mod

def dfs1(i, pre, Edge, Dist, Son, fact, revfact):
    under = 0
    for ne in Edge[i]:
        if ne != pre:
            sonNum = dfs1(ne, i, Edge, Dist, Son, fact, revfact)
            under += sonNum
            Dist[i] *= (comb(under, sonNum, fact, revfact, mod) * Dist[ne]) % mod
            Dist[i] %= mod
    Son[i] = under
    return under + 1 

def solve():
    input = sys.stdin.readline
    N = int(input())
    Edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Edge[a-1].append(b-1)
        Edge[b-1].append(a-1)
    fact = [1] * (N + 1)
    for i in range(1, N + 1): fact[i] = (fact[i-1] * i) % mod
    revfact = [1] * (N + 1)
    revfact[N] = pow(fact[N], mod - 2, mod)
    for i in reversed(range(1, N)): revfact[i] = ((i + 1) * revfact[i+1]) % mod

    Dist = [1] * N
    Son = [0] * N
    dfs1(0, 0, Edge, Dist, Son, fact, revfact)
    q = deque()
    for ne in Edge[0]:
        q.append((ne, 0))
    while q:
        ne, pre = q.pop()
        upper = (Dist[pre] * pow(comb(N - 1, Son[ne] + 1 , fact, revfact, mod), mod - 2, mod)) % mod
        Dist[ne] = (upper * comb(N - 1, N - 1- Son[ne], fact, revfact, mod)) % mod
        for nextEdge in Edge[ne]:
            if nextEdge != pre: q.append((nextEdge, ne))
    print("\n".join(map(str, Dist)))

    return 0

if __name__ == "__main__":
    solve()