import functools
from heapq import*
from collections import deque
import collections
import math
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
inf = float("inf")


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


def modinv(a, mod):
    return modpow(a, mod - 2, mod)


def cnk(a, b):
    MOD = 10**9+7
    ret = 1
    for i in range(b):
        ret *= (a-i)
        ret %= MOD
        ret = ret * modinv(i+1, MOD) % MOD
    return ret


def Dijkstra(n, start, e):
    # input parm e
    # e = [[]for i in range(n)]
    # e[x].append([y, 1])
    # e[y].append([x, 1])
    n += 10

    d = [float("inf") for i in range(n)]
    d[start] = 0

    pathnum = [0 for i in range(n)]
    pathnum[start] = 1

    visited = [False for i in range(n)]
    q = []
    heappush(q, (0, start))
    while len(q):
        now_distance, v = heappop(q)
        if visited[v]:
            continue
        visited[v] = True
        for next_v, next_distance in e[v]:
            if visited[next_v]:
                continue
            dd = now_distance + next_distance
            if d[next_v] > dd:
                d[next_v] = dd
                heappush(q, (dd, next_v))
            if d[next_v] == dd:
                pathnum[next_v] += pathnum[v]
                pathnum[next_v] %= MOD

    return d, pathnum


def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


class UnionFind:
    def __init__(self, n):
        self.sz = [-1 for i in range(n)]

    # 検索
    def find(self, x):
        if self.sz[x] < 0:
            return x
        else:
            self.sz[x] = self.find(self.sz[x])
            return self.sz[x]

    # 併合

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.sz[x] > self.sz[y]:
            x, y = y, x
        self.sz[x] += self.sz[y]
        self.sz[y] = x

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xが含まれている集合のサイズを求める
    def size(self, x):
        return -self.sz[self.find(x)]


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

#
# kruskal
#


@functools.lru_cache(maxsize=None)
class UNION_FIND(object):
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x):
        return -self.parent[self.root(x)]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.size(x) < self.size(y):
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True


def compute_mst_kruskal(max_v, edges):
    edges.sort(key=lambda x: x[2], reverse=1)
    uf = UNION_FIND(max_v)
    mst = []
    for (a, b, c, d) in edges:
        if uf.root(a-1) != uf.root(b-1):
            uf.union(a-1, b-1)
            mst += [d+1]
    return mst


# max_v, max_e = map(int, input().split())
# edges = []
# for i in range(max_e):
#     a, b, c = map(int, input().split())
#     heappush(edges, (a, b, c, i))

# mst = compute_mst_kruskal(max_v, edges)
# mst.sort()
# for i in mst:
#   print(i)

#
# Dinic
#

class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

# V, E, r = map(int, input().split())
# edges = []
# for i in range(E):
#     s, t, d = map(int, input().split())
#     edges.append([s, t, d])

# d = BellmanFord(edges, V, r)
# if d == -1:
#     print("NEGATIVE CYCLE")
#     exit()

# for i in range(V):
#     if d[i] == float("inf"):
#         print("INF")
#     else:
#         print(d[i])


# def BellmanFord(edges, n, s):
#     # グラフの初期化
#     dist = [float("inf") for i in range(n)]
#     dist[s] = 0

#     # 辺の緩和
#     for i in range(n):
#         for edge in edges:
#             if edge[0] != float("inf") and dist[edge[1]] > dist[edge[0]] + edge[2]:
#                 dist[edge[1]] = dist[edge[0]] + edge[2]
#                 if i == n-1 and edge[1] == n - 1:
#                     return -1

#     return dist

ok = [False for i in range(2505)]


def Bellmanford(edges, n, s):
    d = [float("inf") for i in range(n)]
    d[s] = 0

    # 二回辺の緩和をすることで、目的となる点n-1が負の閉路に含まれるか分かる。
    # update = True
    # while update:
    for i in range(n):
        for x, y, z in edges:
            if not ok[x] or not ok[y]:
                continue
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                if i == n - 1:
                    print(-1)
                    exit()
    # d1 = d[n - 1];l
    # print(d)
    # for i in range(n):
    #     for x, y, z in edges:
    #         if d[y] > d[x] + z:
    #             d[y] = d[x] + z
    # print(d)
    print(max(0, -d[n - 1]))


def main():
    n, m, p = map(int, input().split())

    to = [[] for i in range(n + 1)]
    rto = [[] for i in range(n + 1)]
    e = []
    for i in range(m):
        a, b, c = map(int, input().split())
        to[a - 1].append(b - 1)
        rto[b - 1].append(a - 1)
        e.append((a - 1, b - 1, p - c))

    can_reach_to = [False for i in range(n+1)]
    can_reach_rto = [False for i in range(n+1)]

    def todfs(i):
        if can_reach_to[i]:
            return 0
        can_reach_to[i] = True
        for v in to[i]:
            todfs(v)

    def rtodfs(i):
        if can_reach_rto[i]:
            return 0
        can_reach_rto[i] = True
        for v in rto[i]:
            rtodfs(v)
    todfs(0)
    rtodfs(n-1)
    for i in range(n):
        ok[i] = (can_reach_to[i] & can_reach_rto[i])

    d = Bellmanford(e, n, 0)


if __name__ == '__main__':
    main()
