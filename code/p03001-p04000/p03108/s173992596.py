#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

#https://note.nkmk.me/python-union-find/

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
n,m=MI()
lis=[LI() for i in range(m)]
u=UnionFind(n)
def com(x):
    return (x*(x-1))//2
ans=[]
for i in range(m):
    j=m-i-1
    #print(u.group_count())
    x,y=-u.parents[u.find(lis[j][0]-1)],-u.parents[u.find(lis[j][1]-1)]
    u.union(lis[j][0]-1,lis[j][1]-1)
    z=-u.parents[u.find(lis[j][0]-1)]
    delta=com(z)-com(x)-com(y)
    #print(x,y,z)
    #print(max(delta,0))
    ans.append(max(delta,0))
#print(ans)
val=[com(n) for i in range(m)]
for i in range(m-1):
    val[i+1]=val[i]-ans[i]
#print(val)
for i in range(m):
    j=m-i-1
    print(val[j])
    

