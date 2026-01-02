import bisect
import numpy as np
import sys
input = sys.stdin.readline
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

# 二分探索 #
def nibutan(list,n):
	left = -1
	right = len(list)
	while left+1 != right:
		middle = (left+right)//2
		if list[middle] < n:
			left = middle
		else:
			right = middle
	return left+1

N = I()
A = sorted(IL())
B = sorted(IL())
C = sorted(IL())

dp = [0]*(N+1)

for i in range(N):
	dp[i] = nibutan(A,B[i])

num = 0
for i in range(N):
	num += dp[i]
	dp[i] = num

ans = 0
for i in range(N):
	ans += dp[nibutan(B,C[i])-1]

print(ans)