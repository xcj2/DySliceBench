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
    N = int_raw()
    Ws  = ints_raw()
    S2 = sum(Ws)
    S1 = 0
    ans = abs(S2-S1)
    for w in Ws:
        S2-=w
        S1+=w
        ans = min(ans,abs(S2-S1))
    return ans

print(main())
