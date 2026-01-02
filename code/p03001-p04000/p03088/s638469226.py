from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate
import sys



def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


def main():
    n = I()


    def ok(last, c):
        last_plus = last + c
        if 'agc' in last_plus:
            return 0
        for i in range(len(last_plus)-1):
            tmp = list(last_plus)
            tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
            if 'agc' in ''.join(tmp):
                return 0
        return 1



    D = [defaultdict(int) for _ in range(n+1)]
    D[0][''] = 1


    for i in range(n):
        for k, v in D[i].items():
            for c in 'acgt':
                if ok(k, c):
                    D[i+1][(k + c)[-3:]] += v
                    D[i + 1][(k + c)[-3:]] %= mod
    return sum(D[n].values()) % mod





print(main())