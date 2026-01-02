import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()
A = []
for i in range(N):
    A.append(III())

l = 0
for i in range(N):
    for j in range(i+1,N):
        flag = True
        for k in range(N):
            if k==i or k==j:
                continue
            now = A[i][k] + A[k][j]
            if now < A[i][j]:
                print(-1)
                exit()
            if now == A[i][j]:
                flag = False
        if flag:
            l += A[i][j]

print(l)