import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

class UF(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        '''
        x が属するグループを探索
        '''
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        '''
        x と y のグループを結合
        '''
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        '''
        x と y が同じグループか否か
        '''
        return self.find(x) == self.find(y)

    def get_size(self, x):
        '''
        x が属するグループの要素数
        '''
        x = self.find(x)
        return self.size[x]

N,M = II()
p = III()
p = list(map(lambda x:x-1, p))
x,y = Line(M)

place = [0]*N
for i in range(N):
    place[p[i]] = i

uf = UF(N)
for i in range(M):
    uf.union(x[i]-1, y[i]-1)

ans = 0
for i in range(N):
    if uf.is_same(i,place[i]):
        ans += 1

print(ans)