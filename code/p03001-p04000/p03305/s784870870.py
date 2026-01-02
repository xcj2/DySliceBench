# TEST

from math import sin, cos, tan, asin, acos, atan, sqrt, floor, ceil, pi, log10, log, gcd, hypot
from itertools import accumulate, permutations, combinations
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from copy import deepcopy
from decimal import Decimal
import heapq
import sys


sys.setrecursionlimit(10**7)
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n+1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n + 1) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


class BIT():
    # 1,,,,,,,Nまでの数値を扱える
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def to_sum(self, i):
        # i番目のところまでのΣ
        s = 0
        while i > 0:
            s += self.data[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        # i 番目のところに+
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)

    def get(self, i, j):
        # i番目からj番目までの要素のΣ(1<=i<=j<=Nという制約)
        return self.to_sum(j)-self.to_sum(i-1)


class SegTree():
    # 1-indexed
    def __init__(self, lists, function, basement):
        self.n = len(lists)
        self.K = (self.n-1).bit_length()
        self.f = function
        self.b = basement
        self.seg = [basement]*(2**(self.K+1)+1)
        X = 2**self.K
        for i, v in enumerate(lists):
            self.seg[i+X] = v
        for i in range(X-1, 0, -1):
            self.seg[i] = self.f(self.seg[i << 1], self.seg[i << 1 | 1])

    def update(self, k, value):
        X = 2**self.K
        k += X
        self.seg[k] = value
        while k:
            k = k >> 1
            self.seg[k] = self.f(self.seg[k << 1], self.seg[(k << 1) | 1])

    def query(self, L, R):
        num = 2**self.K
        L += num
        R += num
        vL = self.b
        vR = self.b
        while L < R:
            if L & 1:
                vL = self.f(vL, self.seg[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.f(self.seg[R], vR)
            L >>= 1
            R >>= 1
        return self.f(vL, vR)

    def find_max_index(self, L, R, X):
        # [L,R)でX以下の物で最大indexを取得
        return self.fMi(L, R, X, 1, 0, 2**self.K)

    def find_min_index(self, L, R, X):
        # [L,R) でX以下の物で最小のindexを取得する
        return self.fmi(L, R, X, 1, 0, 2**self.K)

    def fMi(self, a, b, x, k, l, r):
        if self.seg[k] > x or r <= a or b <= l:
            # X以上のもの、の時は不等号をself.seg[k]<xにする
            return -1
        else:
            if k >= 2**self.K:
                return k-2**self.K
            else:
                vr = self.fMi(a, b, x, (k << 1) | 1, (l + r) // 2, r)
                if vr != -1:
                    return vr
                return self.fMi(a, b, x, k << 1, l, (l + r) // 2)

    def fmi(self, a, b, x, k, l, r):
        if self.seg[k] > x or r <= a or b <= l:
            # X以上のもの、の時は不等号をself.seg[k]<xにする
            return -1
        else:
            if k >= 2**self.K:
                return k-2**self.K
            else:
                vl = self.fmi(a, b, x, k << 1, l, (l+r)//2)
                if vl != -1:
                    return vl
                return self.fmi(a, b, x, k << 1 | 1, (l+r)//2, r)


class LCA():

    def _bfs(self, node):
        self.visited[node] = True
        for p in tree[node]:
            if self.visited[p] == False:
                self.kprv[0][p] = node
                self.depth[p] = self.depth[node]+1
                self._bfs(p)

    def __init__(self, root, tree):
        self.root = root
        self.n = len(tree)-1
        self.K = (self.n-1).bit_length()
        self.visited = [False for i in range(self.n+1)]
        self.depth = [0 for i in range(self.n+1)]
        self.kprv = [[-1 for i in range(self.n+1)] for j in range(self.K+1)]
        self._bfs(self.root)
        for cnt in range(1, self.K+1):
            for node in range(self.n+1):
                if self.kprv[cnt-1][node] >= 0:
                    self.kprv[cnt][node] = self.kprv[cnt -
                                                     1][self.kprv[cnt-1][node]]
                else:
                    self.kprv[cnt][node] = -1

    def query(self, u, v):
        # u,vの最小共通祖先

        dd = self.depth[v]-self.depth[u]

        if dd < 0:
            u, v = v, u
            dd = -dd

        for i in range(self.K+1):
            if dd & 1:
                v = self.kprv[i][v]
            dd >>= 1
        if u == v:
            return u

        for i in range(self.K-1, -1, -1):
            pu = self.kprv[i][u]
            pv = self.kprv[i][v]
            if pu != pv:
                u = pu
                v = pv
        return self.kprv[0][u]


class Combi():
    def __init__(self, N, mod):
        self.power = [1 for _ in range(N+1)]
        self.rev = [1 for _ in range(N+1)]
        self.mod = mod
        for i in range(2, N+1):
            self.power[i] = (self.power[i-1]*i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod-2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j-1] = (self.rev[j]*j) % self.mod

    def C(self, K, R):
        if K < R:
            return 0
        else:
            return ((self.power[K])*(self.rev[K-R])*(self.rev[R])) % self.mod

    def P(self, K, R):
        if K < R:
            return 0
        else:
            return (self.power[K])*(self.rev[K-R]) % self.mod


class Graph():
    def __init__(self, N, M, Type):
        self._E = M  # 辺の数
        self._V = N  # 頂点の数
        self.type = Type
        if Type == "D":
            # 2次元リスト
            self.G = [[] for i in range(self._V+1)]
        elif Type == "W":
            # 隣接行列
            self.G = [[float("inf") for i in range(self._V+1)]
                             for j in range(self._V+1)]
        elif Type == "B" or Type == "K":
            # 1次元リスト
            self.G = []

    def E(self):
        """ 辺数 """
        return self._E

    @property
    def V(self):
        """ 頂点数 """
        return self._V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self._E += 1
        if self.type == "D":
            self.G[_from].append((_to, _cost))

        elif self.type == "W":
            self.G[_from][_to] = _cost

        elif self.type == "B" or self.type == "K":
            self.G.append((_from, _to, _cost))


class Dijkstra(Graph):
    def __init__(self,N,M,Type):
        super().__init__(N,M,Type)
        self.d = [10**20]*(self._V + 1)
        self.que = []

    def shortest_path(self, s):
        assert self.type == "D"
        heapq.heapify(self.que)
        for i in range(self._V+1):
            self.d[i] = 10**20
        self.d[s] = 0
        heapq.heappush(self.que, (0, s))
        while self.que:
            cost, v = heapq.heappop(self.que)
            if self.d[v] < cost:
                continue

            for node, cost in self.G[v]:
                if self.d[node] > self.d[v] + cost:
                    self.d[node] = self.d[v] + cost
                    heapq.heappush(self.que, (self.d[node], node))
        return self.d


class Bellman_Ford(Graph):
    def __init__(self,N,M,Type):
        super().__init__(N,M,Type)
        self.d = [10**20]*(self._V+1)

    def shortest_path(self, s):
        assert self.type == "B"
        for i in range(self._V+1):
            self.d[i] = 10**20
        self.d[s] = 0
        for _ in range(self._V):
            flag = False
            for From, To, cost in self.G:
                newlen = self.d[From]+cost
                if newlen < self.d[To]:
                    flag = True
                    self.d[To] = newlen
            if not flag:
                break
        return self.d

    def have_negative_circle(self):
        assert self.type == "B"
        for i in range(self._V+1):
            self.d[i] = 10**20
        self.d[1] = 0
        for i in range(1, self._V+1):
            flag = False
            for From, To, cost in self.G:
                newlen = self.d[From]+cost
                if newlen < self.d[To]:
                    flag = True
                    self.d[To] = newlen
            if not flag:
                break
            if i == self._V:
                return True
        return False


class Warshall_Floyd(Graph):

    def __init__(self,N,M,Type):
        super().__init__(N,M,Type)
        self.d = [[10**20 for i in range(self._V+1)] for j in range(self._V+1)]

    def shortest_path(self):
        assert self.type == "W"
        _N = self._V
        for i in range(_N+1):
            for j in range(_N+1):
                self.d[i][j] = self.G[i][j]
        for i in range(_N+1):
            self.d[i][i] = 0
        for k in range(1, _N+1):
            for i in range(1, _N+1):
                for j in range(1, _N+1):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k]+self.d[k][j])
        return d


class Kruskal(Graph):
    def __init__(self,N,M,Type):
        super().__init__(N,M,Type)

    def find_lowest_cost(self):
        res = 0
        self.G.sort()
        connected_G = UnionFind(self._V)
        for p, q, cost in self.G:
            if not connected_G.same(p, q):
                connected_G.union(p, q)
                res += cost
        return res


def union_lcm(lists):
    if len(lists) == 1:
        return lists[0]
    elif len(lists) > 1:
        num = lists[0]
        for i in range(1, len(lists)):
            num = num*lists[i]//gcd(num, lists[i])
        return num


def union_gcd(lists):
    if len(lists) == 1:
        return lists[0]
    elif len(lists) > 1:
        num = lists[0]
        for i in range(1, len(lists)):
            num = gcd(num, lists[i])
        return num


def is_prime(N):
    for i in range(2, N+1):
        if i**2 > N:
            break
        if N % i == 0:
            return False
    return True


class Primes():
    def __init__(self, N):
        self.N = N
        self.prime = {i for i in range(2, self.N+1)}
        for i in range(2, self.N+1):
            if i in self.prime:
                for j in range(i*2, self.N+1, i):
                    if j in self.prime:
                        self.prime.remove(j)

    def show_primes(self):
        return self.prime

    def is_prime(self, X):
        if X < self.N:
            return X in self.prime
        else:
            return "Unknown"


def main():
    # start coding here...

    N, M, S, T = map(int, input().split())
    G1, G2 = Dijkstra(N, M, "D"), Dijkstra(N, M, "D")
    for i in range(M):
        u, v, a, b = map(int, input().split())
        G2.add(u, v, a)
        G2.add(v, u, a)
        G1.add(u, v, b)
        G1.add(v, u, b)
    yen=G2.shortest_path(S)
    snuke=G1.shortest_path(T)
    minimum_case=[10**15 for i in range(N+1)]
    for i in range(N):
        minimum_case[1+i] -= (yen[i+1]+snuke[i+1])
    for i in range(N-1, -1, -1):
        minimum_case[i]=max(minimum_case[i], minimum_case[i+1])
    for i in range(1, N+1):
        print(minimum_case[i])
    return


if __name__ == "__main__":
    main()