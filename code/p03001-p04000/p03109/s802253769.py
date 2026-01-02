#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random
def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return list(input())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A
s = input().split("/")
if int(s[0]) > 2019:
    print("TBD")
elif int(s[0]) == 2019:
    if int(s[1]) > 4:
        print("TBD")
    elif int(s[1]) == 4:
        if int(s[2]) > 30:
            print("TBD")
        else:
            print("Heisei")
    else:
        print("Heisei")
else:
    print("Heisei")
#B