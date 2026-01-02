from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
import pprint
sys.setrecursionlimit(10 ** 9)

INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007

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

def main():
    N = I()
    s = list(S())
    Q = I()
    D = defaultdict(lambda : BIT(N))
    for i in range(N):
        D[s[i]].add(i,1)
    for j in range(Q):
        qi,i,c = LS()
        if qi == "1":
            i = int(i) - 1
            D[s[i]].add(i,-1)
            D[c].add(i,1)
            s[i] = c
        else:
            l,r = int(i)-1, int(c)
            result = 0
            for k in range(97,123):
                if D[chr(k)].interval_sum(l,r):
                    result += 1
            print(result)

if __name__ == '__main__':
    main()