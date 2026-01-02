#!/usr/bin/env pypy3

import sys
sys.setrecursionlimit(10 ** 6)
memo = [1, 1]
def fact(n):
	if len(memo) > n:
		return memo[n]
	else:
		for i in range(len(memo), n+1):
			memo.append(memo[i-1] * i)
		return memo[n]
def nCr(n, r):
	a = 1
	for i in range(r):
		a *= n - i
	return a //fact(r)
def main():
	n = int(sys.stdin.readline())
	a = list(map(int, sys.stdin.readline().split()))
	cnt = {}
	sumcase = 0
	for i in range(n):
		cnt[a[i]] = 0
	for i in range(n):
		cnt[a[i]] += 1
	# print(a, cnt)
	for ai in cnt:
		if cnt[ai] >= 2:
			sumcase += nCr(cnt[ai], 2)
	for i in range(n):
		if cnt[a[i]] == 2:
			print(sumcase - nCr(cnt[a[i]], 2))
		elif cnt[a[i]] > 2:
			#print("hoge", a,  cnt[a[i]], sumcase, cnt)
			print(sumcase - nCr(cnt[a[i]], 2) + nCr(cnt[a[i]]-1, 2))
		else:
			print(sumcase)
main()