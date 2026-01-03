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

    N = I()
    A = LI()
    B = LI()
    uf = UnionFind(N+1)
    Da = defaultdict(list)
    Db = defaultdict(list)
    bita = 0

    same = [False]*(N+1)
    for i in range(N):
        if A[i]==B[i]:
            same[i] = True
    if sum(same)==N:
        print(0)
        return

    for i,a in enumerate(A):
        bita ^= a
        if same[i]:
            continue
        Da[a].append(i)
    Da[bita].append(N)
    bitb = 0
    for i,b in enumerate(B):
        bitb ^= b
        if same[i]:
            continue
        Db[b].append(i)
    Db[bitb].append(N)
    #print(Da)
    #print(Db)
    for key,a in Da.items():
        if len(Db[key])!=len(a):
            print(-1)
            return

    for key,a in Da.items():
        uf.unite(a[0],Db[key][0])
        if len(a)==1:
            continue
        for i in a[1:]:
            uf.unite(a[0],i)
    for b in Db.values():
        if len(b)==1:
            continue
        for i in b[1:]:
            uf.unite(b[0],i)

    if uf.size(N)==N-sum(same):
        ans = uf.size(N)
        if bita!=bitb:
            ans -= 1
        print(ans)
        return

    ans = 0
    used = [False]*(N+1)
    for i in range(N):
        #print(ans)
        if same[i]:
            continue
        p = uf.find(i)
        if used[p]:
            continue
        used[p] = True
        ans += (-uf.parent[p]+1)
        #print(ans)
    #if sum(used)>1:
    #    ans += 1
    if uf.size(N)>1:
        ans -= 1
    if bita!=bitb or len(Da[bita])>1:
        ans -= 1
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

def test():
    i = I()
    li = LI()
    lsi = LSI()
    si = LS()
    print(i)
    print(li)
    print(lsi)
    print(si)
    return

from decimal import Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
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
    examD()

"""
5
0 2 3 6 9
2 9 0 6 3

5
0 2 3 6 9
2 9 0 6 14
# 4
5
0 2 3 6 9
2 3 0 6 14
# 5
5
0 2 3 6 9
2 0 3 9 14
# 5
4
1 2 4 8
2 1 8 4
# 6
"""