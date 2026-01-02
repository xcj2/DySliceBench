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
P = Line(N,1)

place = [-1]*(N+1)
for i in range(N):
    place[P[i]] = i

max_ascend = 0
temp = 1
for i in range(2,N+1):
    if place[i]>place[i-1]:
        temp += 1
    else:
        if max_ascend<temp:
            max_ascend = temp
        temp = 1

if max_ascend<temp:
    max_ascend = temp

print(N-max_ascend)