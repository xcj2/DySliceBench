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

K = I()
A = III()

for i in range(K)[::-1]:
    if i==K-1:
        if A[i]==2:
            l = 2
            r = 3
        else:
            print(-1)
            exit()
    else:
        x = math.ceil(l/A[i])*A[i]
        y = math.floor(r/A[i])*A[i]
        if x<=r and y>=l:
            l = x
            r = y+A[i]-1
        else:
            print(-1)
            exit()

print(l,r)