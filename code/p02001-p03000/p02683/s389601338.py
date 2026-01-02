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

from itertools import product

N,M,X = LI()
C = [0]*N
A = []
for i in range(N):
    x = LI()
    C[i] = x[0]
    A.append(x[1:])

Z = list(product([False,True],repeat=N))
ans = float('inf')
for z in Z:
    cost = 0
    rikai = [0]*M
    for i in range(len(z)):
        if z[i]:
            cost += C[i]
            for j in range(M):
                rikai[j] += A[i][j]
    flag = False
    for i in range(M):
        if rikai[i] < X:
            flag = True
            break
    if not flag:
        if cost < ans:
            ans = cost

if ans == float('inf'):
    print(-1)
else:
    print(ans)