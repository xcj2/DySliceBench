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

N,M = II()
A = III()
B = III()

tate = [False]*(N*M+1)
yoko = [False]*(N*M+1)
for i in range(N):
    tate[A[i]] = True
for j in range(M):
    yoko[B[j]] = True

ans = 1
t_num = 0
y_num = 0
for k in range(1,N*M+1)[::-1]:
    if tate[k] and yoko[k]:
        t_num += 1
        y_num += 1
    elif tate[k]:
        ans *= y_num
        ans %= mod
        t_num += 1
    elif yoko[k]:
        ans *= t_num
        ans %= mod
        y_num += 1
    else:
        ans *= t_num*y_num-(N*M-k)
        ans %= mod

print(ans)