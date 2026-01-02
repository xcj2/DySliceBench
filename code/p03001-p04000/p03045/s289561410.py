import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from collections import deque

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)


    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]


    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def update_all(self):
        for i in range(n+1):
            self.par[i] = self.find(i)


n, m = getList()

UF = UnionFind(n)
for i in range(m):
    a, b, c = getList()
    if not UF.same_check(a, b):
        UF.union(a, b)

UF.update_all()

print(len(list(set(UF.par))) - 1)