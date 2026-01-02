import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


class UnionFind:
    def __init__(self,arg_V):
        self.V = arg_V
        self.boss = [None]*arg_V
        self.height = [None]*arg_V

    def init(self):
        for i in range(self.V):
            self.boss[i] = i
            self.height[i] = 0

    def get_boss(self,index):
        if index == self.boss[index]:
            return index
        else:
            self.boss[index] = self.get_boss(self.boss[index])
            return self.boss[index]


    def is_same_group(self,a,b):
        return self.get_boss(a) == self.get_boss(b)

    def unite(self,x,y):
        boss_x = self.get_boss(x)
        boss_y = self.get_boss(y)

        if boss_x == boss_y:
            return

        if self.height[x] > self.height[y]:

            self.boss[boss_y] = boss_x

        elif self.height[x] < self.height[y]:

            self.boss[boss_x] = boss_y

        else:
            self.boss[boss_y] = boss_x
            self.height[x] += 1

class Edge:
    def __init__(self,arg_FROM,arg_TO,arg_WEIGHT):
        self.FROM = arg_FROM
        self.TO = arg_TO
        self.WEIGHT = arg_WEIGHT

    def __lt__(self,arg):
        return self.WEIGHT < arg.WEIGHT



V,E = map(int,input().split())

UF = UnionFind(V)
UF.init()

table = []

for loop in range(E):
    tmp_from,tmp_to,tmp_cost = map(int,input().split())
    edge = Edge(tmp_from,tmp_to,tmp_cost)
    table.append(edge)

table.sort()

ans = 0

for i in range(E):
    if UF.is_same_group(table[i].FROM, table[i].TO):
        continue
    UF.unite(table[i].FROM, table[i].TO)
    ans += table[i].WEIGHT


print("%d"%(ans))



