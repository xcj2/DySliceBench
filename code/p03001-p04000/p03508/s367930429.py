def examA():
    bit = 41
    N, K = LI()
    A = LI()
    B = [0]*bit
    for a in A:
        for j in range(bit):
            if a&(1<<j)>0:
                B[j] += 1
    ans = 0
    cnt = 0
    for i in range(bit)[::-1]:
        if N-B[i]<=B[i]:
            ans += (1 << i) * B[i]
        else:
            if cnt+(1<<i)>K:
                ans += (1 << i) * B[i]
            else:
                cnt += (1 << i)
                ans += (1 << i) * (N-B[i])
    print(ans)
    return

def examB():
    N, K = LI()
    WP = [LI()for _ in range(N)]
    l = 0; r = 101
    for _ in range(100):
        now = (l+r)/2
        W = [0]*N
        for i,(w,p) in enumerate(WP):
            W[i] = w*(p-now)
        W.sort(reverse=True)
        if sum(W[:K])>=0:
            l = now
        else:
            r = now
    ans = l
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
    N, M = LI()
    Uf = UnionFind(N)
    for _ in range(M):
        a, b = LI()
        a -= 1; b -= 1
        Uf.unite(a,b)
    size = [Uf.size(0),Uf.size(1)]
    size.sort()
    rest = N-sum(size)
    size[1] += rest
    ans = size[0]*(size[0]-1)//2 + size[1]*(size[1]-1)//2 - M
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
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

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examC()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""