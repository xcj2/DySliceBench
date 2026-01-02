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


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


DIV = 10**9+7

def ncr(n, r, mod=DIV):
	r = min(r, n-r)
	ret = 1
	for i in range(1, r+1):
		ret = ret * (n-i+1) % mod
		ret = ret * mod_inv(i, mod) % mod
	return ret


def main():
    ans = 0
    N = int_raw()
    bxys = [ints_raw() for _ in range(N)]
    if N==1:
        return 1
    bxys.sort()
    dtables = {}

    for idx in range(0,N):
        for idx2 in range(idx+1,N):
            dxy = (bxys[idx2][0]-bxys[idx][0],bxys[idx2][1]-bxys[idx][1])
            if dxy in dtables:
                dtables[dxy]+=1
            else:
                dtables[dxy]=1
    dmax = max(dtables.values())
    return N-dmax

print(main())
