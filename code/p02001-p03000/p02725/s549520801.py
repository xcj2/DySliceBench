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

K,N = LI()
A = LI()

A.sort()

x = 0
for i in range(1,N):
    if A[i]-A[i-1] > x:
        x = A[i]-A[i-1]

if K-(A[N-1]-A[0]) > x:
    x = K-(A[N-1]-A[0])

print(K-x)