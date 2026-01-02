# coding: utf-8
# hello worldと表示する
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

'''class UnionFind():
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
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())'''

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
#n,w = map(int,input().split()) #n:頂点数　w:辺の数
n=I()

w=0
d = [[float("inf")]*n for i in range(n)]
for i in range(n):
    d[i][i]=0
mat=[[] for i in range(n)]
for i in range(n):
    s=list(SI())
    for j in range(n):
        if int(s[j])==1:
            w+=1
            d[i][j]=1
            d[j][i]=1
            mat[i].append(j)
            #mat[j].append(i)
col=[0 for i in range(n)]
#print(mat)

col[0]=1
def dfs(x):
    for y in mat[x]:
        if col[y]==0:
            col[y]=(-1)*col[x]
            dfs(y)
        elif col[y]!=col[x]*(-1):
            print(-1)
            exit()
dfs(0)
#print(col)

        
'''nodes=[0 for i in range(2*n)]
uf=UnionFind(2*n)
for i in range(n):
    for j in range(i,n):
        if d[i][j]==1:
            uf.union(i,n+j)
            uf.union(j,n+i)
for i in range(n):
    if uf.same(i,i+n):
        print(-1)
        sys.exit()'''
warshall_floyd(d)
#print(d)
ans=0
for i in range(n):
    for j in range(n):
        if d[i][j]<inf and d[i][j]>ans:
            ans=d[i][j]
print(ans+1)
    

        
    
    
    
    


