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



def div(a, b):
    if a % b:
        return a // b + 1
    return a // b


def main():
    n = I()
    xy = LIR(n)
    x, y = 1, 1
    for nxt_x, nxt_y in xy:
        ratio_x = div(x, nxt_x)
        ratio_y = div(y, nxt_y)
        mul = math.ceil(max(ratio_x, ratio_y))
        x = mul * nxt_x
        y = mul * nxt_y
    return x + y


print(main())