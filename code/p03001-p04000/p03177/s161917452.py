from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from functools import lru_cache
import math

setrecursionlimit(10**6)
rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')
MOD = 10**9 + 7

def mat_mul(A, B):
	n = len(A)
	C = [[0 for __ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				C[i][k] = (C[i][k] + (A[i][j]*B[j][k])) % MOD
	return C

def mat_exp(M, k):
	n = len(M)
	ans = [[0 for __ in range(n)] for _ in range(n)]
	for i in range(n): ans[i][i] = 1
	while k:
		if k % 2 == 1: ans = mat_mul(ans, M)
		k //= 2
		M = mat_mul(M, M)
	return ans

def main():
	n, k = rli()
	A = []
	for _ in range(n):
		A.append(list(rli()))
	M = mat_exp(A, k)
	ans = 0
	for i in range(n):
		for j in range(n):
			ans += M[i][j]
			ans %= MOD
	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()