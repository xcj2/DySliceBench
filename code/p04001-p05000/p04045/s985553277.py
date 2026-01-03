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
    n, k = LI()
    n_list = LI()
    i = n
    while True:
        flag = 0
        for j in n_list:
            if str(j) in str(i):
                flag = 1
        if flag == 0:
            break
        i += 1
    return i





print(main())