def examA():
    N = I()
    ans = (N-1)//2
    print(ans)
    return

def examB():
    N = I()
    D = LI()
    d = Counter(D)
    loop = max(d.keys())
    if D[0]!=0 or d[0]!=1:
        print(0)
        return
#    print(d,loop)
    ans = 1; cur = 1
    for i in range(loop+1):
        if d[i]==0:
            print(0)
            return
        for _ in range(d[i]):
            ans *= cur
            ans %= mod2
        cur = d[i]
    print(ans)
    return

def examC():
    class UnionFind():
        def __init__(self, n):
            self.parent = [-1 for _ in range(n)]
            # 正==子: 根の頂点番号 / 負==根: 連結頂点数

        def find(self, x):
            # 要素xが属するグループの根を返す
            if self.parent[x] < 0:
                return x
            else:
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        def unite(self, x, y):
            # 要素xが属するグループと要素yが属するグループとを併合する
            x, y = self.find(x), self.find(y)
            if x == y:
                return False
            else:
                if self.size(x) < self.size(y):
                    x, y = y, x
                self.parent[x] += self.parent[y]
                self.parent[y] = x

        def same(self, x, y):
            # 要素x, yが同じグループに属するかどうかを返す
            return self.find(x) == self.find(y)

        def size(self, x):
            # 要素xが属するグループのサイズ（要素数）を返す
            x = self.find(x)
            return -self.parent[x]

        def is_root(self, x):
            # すべての根の要素をリストで返す
            return self.parent[x] < 0

        def members(self, x):
            # 要素xが属するグループに属する要素をリストで返す
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def group_count(self):
            # グループの数を返す
            return len(self.roots())

        def all_group_members(self):
            # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
            return {r: self.members(r) for r in self.roots()}
    N = I()
    A = LI()
    B = LI()
    indices = [i for i in range(len(B))]
    sorted_indices = sorted(indices, key=lambda i: B[i])
    sorted_B = [B[i] for i in sorted_indices]
    sorted_A = sorted(A)
#    print(sorted_B); print(sorted_indices)
    d = defaultdict(int)
#    print(sortA,sortB)
    for i in range(N):
        d[sorted_A[i]] = sorted_B[i]
        if sorted_A[i]>sorted_B[i]:
            print("No")
            return
    for i in range(N-1):
        if sorted_A[i+1]<=sorted_B[i]:
            print("Yes")
            return
    uf = UnionFind(N)
    indices_A = [i for i in range(len(A))]
    sorted_indices_A = sorted(indices_A, key=lambda i: A[i])
    for i in range(N):
        uf.unite(sorted_indices[i],sorted_indices_A[i])
    if uf.size(0)<N:
        print("Yes")
        return
    print("No")
    return

def examD():
    class Dijkstra(object):
        """
        construct: O(ElogV)
        """

        def __init__(self, edges, start=0):
            """
            :param list of list of list of int edges:
            :param int start=0:
            """
            self.__dist = [inf] * len(edges)
            self.__dist[start] = 0
            self.__calculate(edges, start)

        @property
        def dist(self):
            return self.__dist

        def __calculate(self, edges, start):
            Q = [(0, start)]  # (dist,vertex)
            while (Q):
                dist, v = heapq.heappop(Q)
                if self.dist[v] < dist: continue  # 候補として挙がったd,vだが、他に短いのがある
                for u, cost in edges[v]:
                    if self.dist[u] > self.dist[v] + cost:
                        self.__dist[u] = self.dist[v] + cost
                        heapq.heappush(Q, (self.dist[u], u))
    N, M = LI()
    V = [[]for _ in range(N)]
    for _ in range(M):
        l, r, c = LI()
        l -=1; r -=1
        V[l].append((r,c))
    for i in range(N-1):
        V[i+1].append((i,0))
#    print(V)
    D = Dijkstra(V)
    ans = D.dist[N-1]
    if ans==inf:
        ans = -1
    print(ans)
    return

def examE():
    N, K = LI()
    ans = [[]for _ in range(N)]


    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examC()

"""

"""