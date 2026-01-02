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

inf = 10**30
N,X,D = II()

if D==0:
    if X==0:
        print(1)
    else:
        print(N+1)
    exit()
if D<0:
    X,D = -X,-D

kukan = []
for i in range(N+1):
    kukan.append([i*X+(i*(i-1)//2)*D, i*X+(N*(N-1)//2-(N-i)*(N-i-1)//2)*D, (i*X)%D])
kukan.sort(key=lambda x:(x[2],x[0]))

div,d_min,d_max = inf,inf,inf
ans = 0
for k in kukan:
    if k[2]!=div:
        if d_min!=inf:
            ans += (d_max-d_min)//D + 1
        d_min,d_max,div = k[0],k[1],k[2]
    else:
        if k[0]>d_max:
            ans += (d_max-d_min)//D + 1
            d_min,d_max = k[0],k[1]
        else:
            d_max = max(d_max,k[1])
ans += (d_max-d_min)//D + 1

print(ans)