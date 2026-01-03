from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
from pprint import pprint

def myinput():
    return map(int,input().split())

def mylistinput(n):
    return [ list(myinput()) for _ in range(n) ]

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

class Kruskal_UnionFind():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edges = []
        self.rank = [0] * N
        self.par = [i for i in range(N)]
        self.counter = [1] * N

    def add(self, u, v, d):
        """
        u = from, v = to, d = cost
        """
        self.edges.append([u, v, d])

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            z = self.counter[x] + self.counter[y]
            self.counter[x], self.counter[y] = z, z
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        x = self.find(x)
        return self.counter[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def Kruskal(self):
        """
        return: 最小全域木のコストの和
        """
        edges = sorted(self.edges, key=lambda x: x[2])  # costでself.edgesをソートする
        res = 0
        for e in edges:
            if not self.same(e[0], e[1]):
                self.unite(e[0], e[1])
                res += e[2]
        return res

n = int(input())
xy = mylistinput(n)

G = Kruskal_UnionFind(n)

xy0 = []
for i in range(n):
    x = xy[i][0]
    y = xy[i][1]
    xy0.append([i,x,y])

xy1 = mysort(xy0,1)
for i in range(n-1):
    No1 = xy1[i][0]
    a = xy1[i][1]
    b = xy1[i][2]
    No2 = xy1[i+1][0]
    c = xy1[i+1][1]
    d = xy1[i+1][2]
    cost = min(abs(c-a),abs(d-b))
    G.add(No1,No2,cost)

xy2 = mysort(xy0,2)
for i in range(n-1):
    No1 = xy2[i][0]
    a = xy2[i][1]
    b = xy2[i][2]
    No2 = xy2[i+1][0]
    c = xy2[i+1][1]
    d = xy2[i+1][2]
    cost = min(abs(c-a),abs(d-b))
    G.add(No1,No2,cost)

ans = G.Kruskal()
print(ans)