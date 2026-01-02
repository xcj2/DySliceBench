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

N,K = LI()
A = LI()

for r in range(K):
    b = [0]*(N+1)
    for i in range(N):
        b[max(0,i-A[i])] += 1
        b[min(N,i+A[i]+1)] -= 1
    cb = [0]*N
    flag = True
    for i in range(N):
        cb[i] = min(cb[i-1]+b[i],N)
        if cb[i] != N:
            flag = False
    A = cb[:]
    if flag:
        break

print(*A)