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


DIV=10**9+7

def mod_invs(n,mod=DIV):
    inv=[0]*(n+1)
    inv[0]=1
    inv[1]=1
    for i in range(2,n+1):
        inv[i] = (-(mod//i)*inv[mod%i]) % mod
    return inv



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
            continue
        else:
            memo[n]=(memo[n-2]+memo[n-1])%DIV
    return memo[-1]

print(main())
