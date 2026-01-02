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
A = [0]*N
x = []
y = []
for i in range(N):
    A[i] = I()
    x0,y0 = Line(A[i],2)
    for j in range(len(x0)):
        x0[j] -= 1
    x.append(x0)
    y.append(y0)

ans = 0
from itertools import product
a = list(product([0,1],repeat=N))

for b in a:
    flag = True
    for i in range(N):
        if b[i]==1:
            for k in range(len(x[i])):
                if b[x[i][k]]!=y[i][k]:
                    flag=False
                    break
    if flag:
        now = sum(b)
        if now>ans:
            ans = now
print(ans)        
