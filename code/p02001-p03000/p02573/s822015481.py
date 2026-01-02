import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


class UnionFind():
    def __init__(self, n):
        """
        Parameters
        ----------
        n:int
            the number of node
        """
        self.par = [-1] * n  # -self.par[i] means the tree size

    def find(self, x):
        """
        Parameters
        ----------
        x:int
            target node

        Return
        ----------
        res:int
            root node
        """
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.par[x] > self.par[y]:  # lesser has many nodes
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        '''
        Parameters
        ----------
        x:int
            target node

        Return
        ----------
        x:int
            size of  group  to which belongs
        '''
        return - self.par[self.find(x)]


n, m = inpl()
uf1 = UnionFind(n)
for _ in range(m):
    a, b = inpl()
    uf1.union(a - 1, b - 1)
for i in range(n):
    uf1.find(i)  # 一周findすることによって接続漏れをなくす。
dp = [1] * n
for i in uf1.par:
    if i >= 0:
        dp[i] += 1
print(max(dp))
