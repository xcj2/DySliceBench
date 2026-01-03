import sys
#import time
import copy
#from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
#import heapq
#import time

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
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
    # xとyが同じグループに属するか判断
    def same(self, x, y):
        return self.find(x) == self.find(y)
    # ノードxが属する木のサイズを返す
    def size(self, x):
        return -self.root[self.find(x)]


n = ri()
d1=[tuple(rl())+tuple((i,)) for i in range(n)]
d2=d1[:]

d1.sort(key=lambda x:x[0])
d2.sort(key=lambda x:x[1])
edge=[]
for i in range(n-1):
    edge.append((d1[i+1][2], d1[i][2],d1[i+1][0]-d1[i][0]))
    edge.append((d2[i+1][2], d2[i][2],d2[i+1][1]-d2[i][1]))


    
edge.sort(key=lambda x: x[2])
res=0
uf = UnionFind(n)
for e in edge:
    if uf.same(e[0], e[1]):
        continue
    uf.unite(e[0], e[1])
    res+=e[2]
print(res)