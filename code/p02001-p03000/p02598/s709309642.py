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

def ceil(a,b):
    return a//b + int(a%b != 0)

N,K = LI()
A = LI()

ok = max(A)
ng = 0

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    count = 0
    for i in range(N):
        count += ceil(A[i],mid)-1
    if count <= K:
        ok = mid
    else:
        ng = mid

print(ok)