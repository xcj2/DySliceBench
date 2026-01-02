'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7 #998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

#UnionFindのクラス,0-indexed
class UnionFind():
    def __init__(self, n):
        self.n = n
        # parents = [-1,0,-4,1,1,1]のように、親の添字かマイナス要素数を表す
        self.parents = [-1] * n
    # find: xの親がすべてrootになる。これにより計算量削減(O(N) for all (not each))
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
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    n,m = map(int,ipt().split())
    uf = UnionFind(n+1)
    for i in range(m):
        a,b = map(int,ipt().split())
        uf.union(a,b)

    print(-min(uf.parents))

    return None

if __name__ == '__main__':
    main()
