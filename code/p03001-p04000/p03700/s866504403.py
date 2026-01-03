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

N,A,B = II()
h = Line(N,1)

left = -1
right = 10**9

while abs(right-left)>1:
    mid = (right+left)//2
    counter = 0
    for i in range(N):
        if h[i]>mid*B:
            counter += math.ceil((h[i]-mid*B)/(A-B))
    if counter<=mid:
        right = mid
    else:
        left = mid

print(right)