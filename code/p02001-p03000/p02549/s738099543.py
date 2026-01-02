from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from math import gcd
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]




class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size
        self.total = 0

    def add(self, i, w):
        x = i + 1
        self.total += w
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def interval_sum(self, i, j): # i <= x < j の区間
        return self.sum(j - 1) - self.sum(i - 1) if i else self.sum(j - 1)


mod=998244353
n,k=LI()
lr=LIR(k)
bit=BIT(n+1)
bit.add(0,1)
for i in range(n):
    ret=0
    for j in range(k):
        l,r=lr[j]
        if i-l+1>0:
            ret+=bit.interval_sum(max(i-r,0),i-l+1)
    bit.add(i,ret%mod)
    ans=ret%mod

print(ans)




