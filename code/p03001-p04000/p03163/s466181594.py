from copy import *
from sys import *
from math import *
import queue
from collections import defaultdict,Counter,deque

setrecursionlimit(1000000)

#dp[i][w]
def main():
	n,w = map(int,input().split())
	wv = [list(map(int,input().split())) for i in range(n)]
	dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
	for i in range(1,n+1):
		cw = wv[i-1][0]
		cv = wv[i-1][1]
		for j in range(w+1):
			dp[i][j] = max(dp[i-1][j],dp[i-1][j-cw] + cv) if j-cw >= 0 else dp[i-1][j]
	print(dp[-1][-1])

def zip(a):
	mae = a[0]
	ziparray = [mae]
	for i in range(1,len(a)):
		if(mae != a[i]):
			ziparray.append(a[i])
			mae = a[i]
	return ziparray

def base_10_to_n(X, n):
	X_dumy = X
	out = ''
	while X_dumy>0:
		out = str(X_dumy%n)+out
		X_dumy = int(X_dumy/n)
	if(out == ''): return '0'
	return out

def gcd(m,n):
	x = max(m,n)
	y = min(m,n)
	while(x%y!=0):
		z = x%y
		x = y
		y = z
	return y

class Queue():
	#競プロ用のQueue
	def __init__(self):
		self.q = deque([])
	def push(self,i):
		self.q.append(i)
	def pop(self):
		return self.q.popleft()
	def size(self):
		return len(self.q)

class Stack():
	#怯プロ用のStack
	def __init__(self):
		self.q = []
	def push(self,i):
		self.q.append(i)
	def pop(self):
		return self.q.pop()
	def size(self):
		return len(self.q)

main()