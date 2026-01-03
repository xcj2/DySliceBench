import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()
A = LI()
A.sort()

cusum = [0]*N
cusum[0] = A[0]
for i in range(1,N):
    cusum[i] = cusum[i-1]+A[i]

lim = 0
for i in range(N-1)[::-1]:
    if cusum[i]*2 < A[i+1]:
        lim = i+1
        break

print(N-lim)