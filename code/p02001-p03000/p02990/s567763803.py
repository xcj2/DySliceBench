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
    N,K = ints_raw()
    anses = [0]*K
    #anses [1] = (N-K+1)%DIV
    NR = N-K
    for i in range(1,K+1):
        divBK = ncr(K-1,i-1)
        convR = 0
        if NR >= i-1:
            convR = ncr(NR-i+1+i,i)
        anses[i-1]=(divBK*convR)%DIV
    return "\n".join(map(str,anses))


print(main())
