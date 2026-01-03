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
	n, a = LI()
	x_list = np.array(LI())
	nx = n*max(x_list+[a])
	y_list = x_list - a
	dp = np.full((n+1,2*nx+1),INF)

	def dfs(j,t):
		dp_value = dp[j,t]
		if dp_value == INF:
			if j == 0 and t == nx:
				dp_value = 1
			elif j >= 1 and (y_list[j-1] < t - 2*nx or y_list[j-1] > t):
				dp_value = dfs(j-1, t)
			elif j >= 1 and 0 <= t - y_list[j-1] <= 2*nx:
				dp_value = dfs(j-1, t) + dfs(j-1, t-y_list[j-1])
			else:
				dp_value = 0
			dp[j,t] = dp_value
		return int(dp_value)

	print(dfs(n, nx) -1)


if __name__ == '__main__':
    main()