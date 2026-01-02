import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
Max = sys.maxsize
def ll():
	return list(map(int,input().split()))
def m():
	return map(int,input().split())
def onem():
	return int(input())
def s(x):
	a = []
	aa = x[0]
	su = 1
	for i in range(len(x)-1):
		if aa == x[i+1]:
			a.append([aa,su])
			aa = x[i+1]
			su = 1
		else:
			su += 1
	a.append([aa,su])
	return a
def jo(x):
	return " ".join(map(str,x))

h,w = m()

l = []

for i in range(h):
	a = ll()
	l.append(a)

dp = [[0 for i in range(w+1)] for j in range(h+1)]

for i in range(h):
	for j in range(w):
		if l[i][j] == 0:
			dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j]) + 1
print(max(map(max,dp))**2)




