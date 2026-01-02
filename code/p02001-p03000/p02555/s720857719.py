from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from functools import lru_cache
import math

#setrecursionlimit(10**6)
rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')
MOD = 10**9 + 7

def main():
	s = int(rl())

	def binom_tables(n, q):
		fact = [1 for _ in range(n + 1)]
		inv = [1 for _ in range(n + 1)]
		for i in range(1, n+1):
			fact[i] = (fact[i-1] * i) % q
			inv[i] = pow(fact[i], q-2, q)
		return fact, inv

	F, I = binom_tables(s + s//3 + 10, MOD)

	def binom(n, k, q):
		return (F[n]*((I[k]*I[n-k])%q))%q

	ans = 0
	for r in range(1, 700):
		objects = s - 3*r
		if objects < 0: break
		x = binom(objects + r - 1, objects, MOD)
		ans += x
		ans %= MOD 

	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()