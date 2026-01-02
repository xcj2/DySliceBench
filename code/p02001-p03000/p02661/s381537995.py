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
A,B = LIR(N,2)
A.sort()
B.sort()

if N%2 == 1:
    min_ = A[(N-1)//2]
    max_ = B[(N-1)//2]
    print(max_-min_+1)
else:
    smin_ = A[N//2-1]+A[N//2]
    smax_ = B[N//2-1]+B[N//2]
    print(smax_-smin_+1)