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
mod = 10**9+7
alp = "abcdefghijklmnopqrstuvwxyz"
dir = [(-1,0),(0,-1),(1,0),(0,1)]

#UnionFindのクラス,0-indexed
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
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
    h,w = map(int,ipt().split())
    brd = [input()+"-" for i in range(h)]
    brd.append("-"*(w+1))
    d = {"#":0, ".":1, "-":-4}
    al = [True]*(h*w)
    ans = 0

    for i in range(h):
        for j in range(w):
            if al[i*w+j]:
                q = [(i,j)]
                al[i*w+j] = False
                nm = [0,0]
                nm[d[brd[i][j]]] += 1
                while q:
                    qi,qj = q.pop()
                    qs = d[brd[qi][qj]]
                    for di,dj in dir:
                         ni = qi+di
                         nj = qj+dj
                         if d[brd[ni][nj]] == 1-qs and al[ni*w+nj]:
                             al[ni*w+nj] = False
                             nm[1-qs] += 1
                             q.append((ni,nj))
                ans += nm[0]*nm[1]

    print(ans)





    return None

if __name__ == '__main__':
    main()
