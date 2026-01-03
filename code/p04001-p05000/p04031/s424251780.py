from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random

def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LIM(): return list(map(lambda x:int(x) - 1, input().split()))
def LS(): return input().split()
def S(): return input()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007



def main():
    n = I()
    n_list =  sorted(LI())
    ans = float('inf')
    for i in range(n_list[0], n_list[-1] + 1):
        ret = 0
        for j in n_list:
            ret += (i - j) ** 2
        ans = min(ans, ret)


    return ans








print(main())