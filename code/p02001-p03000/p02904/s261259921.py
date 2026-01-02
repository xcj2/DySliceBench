def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
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
            # 要素の根をリストで返す
            return self.parent[x] < 0

        def roots(self):
            # すべての根の要素をリストで返す
            return [i for i, x in enumerate(self.parent) if x < 0]

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
    class segment_():
        def __init__(self, A, n, segfunc,ide_ele):
            #####単位元######要設定0or1orinf
            self.ide_ele = ide_ele
            ####################
            self.num = 1 << (n - 1).bit_length()
            self.seg = [self.ide_ele] * 2 * self.num
            self.segfunc = segfunc
            # set_val
            for i in range(n):
                self.seg[i + self.num] = A[i]
                # built
            for i in range(self.num - 1, 0, -1):
                self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

        def update(self, k, r):
            k += self.num
            self.seg[k] = r
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        # 値xに1加算
        def update1(self, k):
            k += self.num
            self.seg[k] += 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def updateneg1(self, k):
            k += self.num
            self.seg[k] -= 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def query(self, p, q):
            if q < p:
                return self.ide_ele
            p += self.num;
            q += self.num
            res = self.ide_ele
            while p < q:
                if p & 1 == 1:
                    res = self.segfunc(res, self.seg[p])
                    p += 1
                if q & 1 == 1:
                    q -= 1
                    res = self.segfunc(res, self.seg[q])
                p >>= 1;
                q >>= 1
            return res
    N, K = LI()
    P = LI()
    Seg_min = segment_(P, N, lambda a, b: min(a,b),inf)
    Seg_max = segment_(P, N, lambda a, b: max(a, b),-inf)
    DL = defaultdict(bool)
    DR = defaultdict(bool)
    for i in range(N-K+1):
        cur = Seg_min.query(i,i+K)
        if cur==P[i]:
            DL[i] = True
        cur = Seg_max.query(i,i+K)
        if cur==P[i+K-1]:
            DR[i+K-1] = True
    #print(DL,DR)
    uf = UnionFind(N)
    bigger = [False]*N
    skip = []
    for i in range(N-1):
        if P[i+1]>P[i]:
            bigger[i] = True
    cur = sum(bigger[:K-1])
    if cur == K - 1:
        skip.append(0)
    for i in range(N-K):
        if bigger[i+K-1]:
            cur += 1
        if bigger[i]:
            cur -= 1
        if cur==K-1:
            skip.append(i+1)
    #print(skip)
    #print(bigger)
    for i in range(len(skip)-1):
        uf.unite(skip[i],skip[i+1])

    for i in range(N-K):
        if DL[i] and DR[i+K]:
            uf.unite(i,i+1)
    ans = set()
    for i in range(N-K+1):
        cur = uf.find(i)
        #print(i,cur)
        ans.add(cur)
    print(len(ans))
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()

"""
9 4
8 0 1 2 3 4 5 6 7 

9 2
6 7 8 3 4 5 0 1 2

13 4
9 10 11 12 2 1 0 6 7 8 3 4 5
"""