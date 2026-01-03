import sys
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10*5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

class UnionFind():

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)

        if(x == y):
            return 

        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1


    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]

n, k, l = MAP()
road = [0]*k
train = [0]*l
for i in range(k):
    p, q = MAP()
    road[i] = (p,q)
for i in range(l):
    r, s = MAP()
    train[i] = (r,s)

ans = [0]*n

uf_road = UnionFind(n)
uf_train = UnionFind(n)

for i in range(k):
    uf_road.Unite(road[i][0]-1, road[i][1]-1)
for i in range(l):
    uf_train.Unite(train[i][0]-1, train[i][1]-1)

roots = [(0,0)]*n
for i in range(n):
    a = uf_road.Find_Root(i)
    b = uf_train.Find_Root(i)
    roots[i] = (a, b)

c = Counter(roots)
for i in range(n):
    ans[i] = c[roots[i]]

for i in range(n):
    print(str(ans[i]) + " ", end = "")

    