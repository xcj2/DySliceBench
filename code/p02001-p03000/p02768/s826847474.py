import heapq
import sys
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

import functools
@functools.lru_cache(maxsize=None)
def tami(n, x):
	if x == 1:
		return n
	elif x%2 == 0:
		return tami(n, x//2)**2 %mod
	else:
		return tami(n, x-1)*n %mod

def nCr(n, r):
	r = min(r, n-r)
	numer = denom = 1
	for i in range(1, r+1):
		numer = numer * (n+1-i) % mod
		denom = denom * i % mod
	return numer * pow(denom, mod-2, mod) % mod

N,a,b = IL()

n = tami(2, N) -1
aa = nCr(N, a)
bb = nCr(N, b)
ans = n-aa-bb
while ans < 0:
	ans += mod
print(ans)