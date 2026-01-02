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

N,T = II()
A,B = Line(N,2)

m1 = [[0]*(T+1) for _ in range(N)]
m2 = [[0]*(T+1) for _ in range(N)]

for i in range(N):
    for t in range(T+1):
        if i==0:
            if t-0.5>=A[i]:
                m1[i][t] = B[i]
            else:
                pass
        else:
            if t-0.5>=A[i]:
                m1[i][t] = max(m1[i-1][t-A[i]]+B[i], m1[i-1][t])
            else:
                m1[i][t] = m1[i-1][t]

for i in range(N):
    for t in range(T+1):
        if i==0:
            m2[i][t] = B[i]
        else:
            val1 = m1[i-1][t] + B[i]
            if t-A[i]-0.5>=0:
                val2 = max(m2[i-1][t], m2[i-1][t-A[i]]+B[i])
            else:
                val2 = m2[i-1][t]
            m2[i][t] = max(val1,val2)

print(m2[N-1][T])