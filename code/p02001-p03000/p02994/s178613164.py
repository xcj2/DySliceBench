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
    
def mod_modify(a,mod):
    return (a+mod)%mod
    
def main():
    ans =0
    N,L = ints_raw()
    if L<0:
        if L+N-1 >=0:
            return sum([L+i for i in range(N)])
        else:
            return sum([L+i for i in range(N-1)])
    for i in range(1,N):
        ans+=(L+i)
    return ans

print(main())
