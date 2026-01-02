def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    #############################################################
    class UnionFind():
        def __init__(self, n):
            self.parent = [-1 for _ in range(n)]
            self.n = n
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
    ################################################################################
    N, M = LI()
    a = LI()
    ans = 0
    uf = UnionFind(N)
    for _ in range(M):
        x,y = LI()
        if not uf.same(x,y):
            uf.unite(x,y)
    D = defaultdict(int)
    rep = defaultdict(bool)
    r = uf.roots()
    keep = [-1]*N
    for i in range(N):
        parent = uf.find(i)
        if (not D[parent]) or D[parent] > a[i]:
            D[parent] = a[i]
            keep[parent] = i
    for i in range(N):
        if keep[i]==-1:
            continue
        rep[keep[i]] = True
        ans += D[i]
    loop = uf.group_count()-2
    if loop==-1:
        print(0)
        return
    A = []
    for i,j in enumerate(a):
        A.append([j,i])
    A.sort()
    cur = 0
    for i in range(N):
        if cur>=loop:
            break
        if not rep[A[i][1]]:
            cur +=1
            ans += A[i][0]
    if cur<loop:
        print("Impossible")
        return
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
    examD()

"""

"""