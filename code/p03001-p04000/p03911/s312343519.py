import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from itertools import combinations

# Union Find
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

N,M = LI()
uf = UF(N+M)
for i in range(N):
    kl = LI()
    for l in kl[1:]:
        uf.union(i,N+l-1)

root = uf.find(0)
for i in range(1,N):
    now = uf.find(i)
    if now != root:
        print('NO')
        exit()
print('YES')