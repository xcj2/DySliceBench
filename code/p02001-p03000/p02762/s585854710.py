from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
"""
#N,K,Mが入力
    n,k,m=LI() 
    #N
    #x1 y1
    #.  .
    #xn ynが入力
    N=I()
    p=LIR(N)
    print(n,k,m,p)
"""

############################## ユニオン木(union tree) ###################################
#uf=UnionFind(n)と使う
# print(uf.roots())
# print(uf.all_group_members())
class UnionFind:
    def __init__(self, n):
        self.n=n
        self.par = [-1 for i in range(self.n+1)]
        self.rank = [0 for i in range(self.n+1)]#素集合でないとrankは意味がなさそう,素集合であればrank kには少なくとも2^k要素がある。
    
    # 検索
    def find(self, x):
        # if self.par[x] == x:
        if self.par[x] <0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[y]+=self.par[x]
            self.par[x] = y
        else:
            self.par[x]+=self.par[y]
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n+1) if self.find(i) == root]

    def size(self, x):
        return -self.par[self.find(x)]

    #すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.par) if x<0]

    #グループの数を返す
    def group_count(self):
        return len(self.roots())

    #{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {int(r):self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
   
   

def resolve():
    n,m,k=LI()
    A=LIR(m)
    C=LIR(k)

    uf=UnionFind(n-1)
    # ub=UnionFind(n-1)
    dame=[[] for i in range(n)]
    for i in range(m):
        a=A[i][0]-1
        b=A[i][1]-1
        dame[a].append(b)
        dame[b].append(a)
        uf.union(a,b)

    for i in range(k):
        c=C[i][0]-1
        d=C[i][1]-1
        if uf.same(c,d)==True:
            dame[c].append(d)
            dame[d].append(c)
        # ub.union(c,d)

    # d=uf.all_group_members()
    # print(d)
    ans=[0]*n
    for i in range(n):
        ans[i]=str((uf.size(i)-1-len(dame[i])))
    L=' '.join(ans)

    print(L)


import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """4 4 1
2 1
1 3
3 2
3 4
4 1"""
        output = """0 1 0 1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 10 0
1 2
1 3
1 4
1 5
3 2
2 4
2 5
4 3
5 3
4 5"""
        output = """0 0 0 0 0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1"""
        output = """1 3 5 4 3 3 3 3 1 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
