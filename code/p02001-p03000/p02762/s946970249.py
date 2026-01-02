import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
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

class UnionFind():
    def __init__(self, n):
        """
        Parameters
        ----------
        n:int
            the number of node
        """
        self.par = [-1] * n # -self.par[i] means the tree size

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
            if self.par[x] > self.par[y]: # lesser has many nodes
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
        

n, m, k = inpl()
dame = collections.defaultdict(set)
uf = UnionFind(n)
ans=[0]*n
for i in range(m):
    a, b = inpl()
    a, b = a - 1, b - 1
    dame[a].add(b)
    dame[b].add(a)
    uf.union(a,b)
for i in range(k):
    c, d = inpl()
    c, d = c - 1, d - 1
    if uf.is_same(c,d):
        dame[c].add(d)
        dame[d].add(c)
for i in range(n):
    ans[i] = uf.size(i) - len(dame[i]) - 1
    # 同じグループに所属 - (友達+ブロック) - 自分
print(*ans)

'''

'''