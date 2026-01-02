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
def resolve():
    n,m=LI()
    s=LIR(m)
    ans=0
    for i in range(m):
        uf=UnionFind(n)
        for j in range(m):
            if i!=j:
                a,b=s[j][0],s[j][1]
                uf.union(a,b)

        if len(uf.roots())>2:
            ans+=1

    print(ans)
    return
"""
7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7
        output = 4
"""


############################## ユニオン木(union tree) ###################################
#uf=UnionFind(n)と使う
# print(uf.roots())
# print(uf.all_group_members())
class UnionFind:
    def __init__(self, n):
        self.n=n
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)#素集合でないとrankは意味がなさそう,素集合であればrank kには少なくとも2^k要素がある。
    
    # 検索
    def find(self, x):
        if self.par[x] == x:
        #if self.par[x] <0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
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

    #すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.par) if i==x]

    #グループの数を返す
    def group_count(self):
        return len(self.roots())

    #{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {int(r):self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    

#辞書やタプルで使えるようにクラスを継承 l = ['A', 'B', 'C', 'D', 'E']とかを想定
class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * (self.n)
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    #def size(self, x):
    #    return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]



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
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 5
1 2
2 3
3 4
4 5
5 6"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()