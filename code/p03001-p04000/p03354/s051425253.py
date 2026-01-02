# abcde    s=input()    s='abcde'
# abcde    s=list(input())    s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)    a=int(input())    a=5
# 1 2    | x,y = s_inpl()   |    x=1,y=2
# 1 2 3 4 5 ... n 　    li = input().split()    li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　    li = inpl()    li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　    li = input().split('T')    li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]

import math
import copy
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right
# import numpy as np

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")
MAX_DIGIT = 50

############
############
############

class UnionFind(object):
 
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
 
        if self.rank[x] < self.rank[y]:
            x, y = y, x
 
        self.size[x] += self.size[y]
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def count(self, x):
        return self.size[self.find(x)]

N, M = l_inpl()
p = l_inpl()

uf = UnionFind(N)
for _ in range(M):
    xi, yi = l_inpl()
    xi, yi = xi-1, yi-1
    uf.union(xi, yi)

ans = 0
for i, pi in enumerate(p):
    pi = pi - 1
    if uf.same(i, pi):
        ans += 1

print(ans)    
