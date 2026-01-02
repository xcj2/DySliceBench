# @uthor : Kaleab Asfaw
from sys import stdin, stdout
# Fast IO
# from math import gcd

def input():
	a = stdin.readline()
	if a[-1] == "\n": a = a[:-1]
	return a
def print(*argv, end="\n", sep=" "):
	n = len(argv)
	for i in range(n):
		if i == n-1: stdout.write(str(argv[i]))
		else: stdout.write(str(argv[i]) + sep)
	stdout.write(end)
# Others
mod = 10**9+7
def lcm(x, y): return (x * y) / (gcd(x, y))
def fact(x, mod=mod):
	ans = 1
	for i in range(1, x+1): ans = (ans * i) % mod
	return ans
def arr2D(n, m, default=0):
	lst = []
	for i in range(n): temp = [default] * m; lst.append(temp)
	return lst
def sortDictV(x): return {k: v for k, v in sorted(x.items(), key = lambda item : item[1])}

def solve(n):
	c = [x for x in range(3, 2001)]
	dp = [float("-inf")] * (n+1)
	dp[0] = 1
	for i in range(1, n+1):
		s = 0
		for x in c:
			if i - x >= 0:
				s += dp[i-x]
		dp[i] = s % mod
	return dp[n]

n = int(input())
print(solve(n))