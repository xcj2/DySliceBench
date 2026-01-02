import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def main():
    N,M = ints_raw()
    As = [int_raw() for _ in range(M)]
    is_breake = [0]*(N+1)
    for a in As:
        is_breake[a]=1
    memo = [0]*(N+1)
    memo[0]=1
    memo[1]=1 if is_breake[1]==0 else 0
    for n in range(2,N+1):
        if is_breake[n]:
            memo[n] =0
            
        else:
            memo[n]=(memo[n-2]+memo[n-1])%DIV
    return memo[-1]

print(main())
