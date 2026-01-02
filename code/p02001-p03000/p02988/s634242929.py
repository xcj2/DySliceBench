from heapq import heappush, heappop
import re
from collections import deque
import sys
input = sys.stdin.readline


def int_raw():
    return int(input())


def ss_raw():
    return input().split()


def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def mod_invs(n, mod=DIV):
    inv = [0]*(n+1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, n+1):
        inv[i] = (-(mod//i)*inv[mod % i]) % mod
    return inv


def main():
    N= int_raw()
    ps = ints_raw()
    ans =0
    for i in range(1,N-1):
        p = ps[i]
        p_sub = ps[i-1:i+2]
        if(min(p_sub)!=p and max(p_sub)!=p):
            ans+=1
    return ans

print(main())
