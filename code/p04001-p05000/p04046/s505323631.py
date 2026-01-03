import sys
import numpy as np
import random
from decimal import Decimal
import itertools
import re
import bisect
from collections import deque, Counter
from functools import lru_cache

sys.setrecursionlimit(10**9)
INF = 10**13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
def SERIES(n): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ')
def GRID(h,w): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ').reshape(h,-1)[:,:w]
def GRIDfromString(h,w): return np.frombuffer(sys.stdin.buffer.read(), 'S1').reshape(h,-1)[:,:w]
MOD = 1000000007



def main():
	h, w, a, b = LI()

	def comb(n, r, p):
		if (r < 0) or (n < r):
			return 0
		r = min(r, n - r)
		return fact[n] * factinv[r] * factinv[n-r] % p


	p = 10 ** 9 + 7
	N = 10 ** 5 * 2
	fact = [1, 1]
	factinv = [1, 1]
	inv = [0, 1]

	for i in range(2, N + 1):
		fact.append((fact[-1] * i) % p)
		inv.append((-inv[p % i] * (p // i)) % p)
		factinv.append((factinv[-1]) * inv[-1] % p)

	ans = 0
	for i in range(1,w-b+1):
		ans += comb(h-a+b+i-2, max(h-a-1, b+i-1), MOD) * comb(a+w-b-i-1, max(a-1, w-b-i), MOD)
		ans %= MOD
	print(ans)


if __name__ == '__main__':
    main()