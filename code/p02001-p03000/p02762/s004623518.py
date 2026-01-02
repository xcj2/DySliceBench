# coding: utf-8

import sys
import math
import collections
import itertools
from inspect import currentframe
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def MI() : return map(int, input().split())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def chkprint(*args) : names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}; print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

class UnionFind:
    def __init__(self, n):
        # 負 : 根である．絶対値はランク
        # 正 : 根じゃない．値は親の番号
        self.root_table = [-1] * n
        # 自分の下に何個あるか(自分含む)
        self.count_table =  [1] * n
 
    def get_root(self, x):
        if self.root_table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.root_table[x] = self.get_root(self.root_table[x])
            return self.root_table[x]
 
    def find(self, x, y):
        return self.get_root(x) == self.get_root(y)
 
    def union(self, x, y):
        r1 = self.get_root(x)
        r2 = self.get_root(y)
        if r1 == r2:
            return

        # ランクの取得
        d1 = self.root_table[r1]
        d2 = self.root_table[r2]
        # 値が小さいほど深い木である(絶対値が大きい)
        if d1 <= d2:
            self.root_table[r2] = r1
            self.count_table[r1] += self.count_table[r2]
            # 深さが同じ時はランクが増える
            if d1 == d2:
                self.root_table[r1] -= 1
        else:
            self.root_table[r1] = r2
            self.count_table[r2] += self.count_table[r1]
        
    def count(self, x):
        return self.count_table[self.get_root(x)]


N, M, K = MI()
AB = LRI(M)
CD = LRI(K)

uf = UnionFind(N + 1)
friend = [0] * (N + 1)

for ab in AB:
    a, b = ab

    friend[a] -= 1
    friend[b] -= 1

    uf.union(a, b)

for cd in CD:
    c, d = cd

    if uf.find(c, d):
        friend[c] -= 1
        friend[d] -= 1

for i in range(1, N + 1):
    friend[i] += (uf.count(i) - 1)

print(*friend[1:])
