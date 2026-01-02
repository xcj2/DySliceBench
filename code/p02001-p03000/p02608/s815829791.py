# @uthor : Kaleab Asfaw
from sys import stdin, stdout
# Fast IO
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
def comb(lst, x):
	from itertools import combination as c
	return list(comb(lst, x))
def fact(x, mod=mod):
	ans = 1
	for i in range(1, x+1): ans = (ans * i) % mod
	return ans
def arr2D(n, m, default=0):
	lst = []
	for i in range(n): temp = [default] * m; lst.append(temp)
	return lst
def sortDictV(x): return {k: v for k, v in sorted(x.items(), key = lambda item : item[1])}
def smaller(lst, x): return bisect_left(lst, x) -1
def smallerEq(lst, x): return bisect_right(lst, x) -1

def solve(n):
	lst = [0] * 10000
	for i in range(1, 101):
		for j in range(1, 101):
			for k in range(1, 101):
				val = (i**2) + (j**2) + (k**2) + (i*j) + (i*k) + (j*k)
				if val >= 1 and val <= 10000:
					lst[val-1] += 1
	for i in range(0, n):
		print(lst[i])

n = int(input())
solve(n)