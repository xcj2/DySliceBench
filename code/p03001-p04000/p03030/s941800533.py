import bisect
from operator import itemgetter
import math
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
SP = []

for i in range(N):
    s,p = SL()
    SP.append([s,int(p),i+1])

sp = sorted(SP,key=itemgetter(1),reverse=True)
sp = sorted(sp,key=itemgetter(0))

for i,j,k in sp:
    print(k)