#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]


#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

import heapq

N = I()
A = III()
B = III()

x = []
for i,b in enumerate(B):
    heapq.heappush(x,(-b,i))

counter = 0

while x:
    temp = heapq.heappop(x)
    i = temp[1]
    b = -temp[0]
    a = B[(i-1)%N]
    c = B[(i+1)%N]
    if b == A[i]:
        continue
    elif b<A[i]:
        print(-1)
        exit()
    else:
        d,m = divmod(b-A[i],a+c)
        if d==0:
            print(-1)
            exit()
        elif m == 0:
            B[i] = A[i]
            counter = counter+d
        else:
            B[i] = A[i]+m
            heapq.heappush(x,(-B[i],i))
            counter = counter+d

print(counter)