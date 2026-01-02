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

N,M = IL()

A = IL()
BC = [IL() for i in range(M)]
A.sort()
BC.sort(key=itemgetter(1),reverse=True)

tmp = bisect.bisect_left(A,BC[0][1])
cnt = 0
j = 0
for b,c in BC:
    for i in range(b):
        if c > A[j]:
            A[j] = c
            j += 1
            cnt += 1
            if cnt == tmp:
                break
        else:
            break
    else:
        continue
    break

print(sum(A))