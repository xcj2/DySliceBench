from heapq import heappush, heappop
import re
from collections import deque
import sys
import math
input = sys.stdin.readline


def int_raw():
    return int(input())


def ss_raw():
    return input().split()


def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)


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


def ncr(n, r, mod=DIV):
	r = min(r, n-r)
	ret = 1
	for i in range(1, r+1):
		ret = ret * (n-i+1) % mod
		ret = ret * mod_inv(i, mod) % mod
	return ret


def main():
    N = int_raw()
    Ss = [input().strip("\n") for i in range(N)]
    hist_ana = {}
    for s in Ss:
        hist = [0]*27
        for c in s:
            hist[ord(c)-ord("a")]+=1
        hist = tuple(hist)
        if hist in hist_ana:
            hist_ana[hist]+=1
        else:
            hist_ana[hist]=1
    return sum([l*(l-1)//2 for k,l in hist_ana.items()])
    
print(main())
