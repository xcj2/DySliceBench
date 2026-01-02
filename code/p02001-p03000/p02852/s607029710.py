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

from bisect import bisect_right

N,M = II()
A = str(input())

B = A[::-1]

ans = []
place = 0
while place!=N:
    for i in range(1,M+1)[::-1]:
        if place+i<=N:
            if B[place+i]!='1':
                ans.append(i)
                place += i
                break
        if i==1 and B[place+i]=='1':
            print(-1)
            exit()

print(*list(reversed(ans)))