from copy import *
from sys import *
from math import *
import queue
from collections import defaultdict,Counter,deque

setrecursionlimit(1000000)

#dp[x][y] 最終日にyを選択した際のx日目までの最大の幸福度
def main():
	n = int(input())
	abc = [list(map(int, input().split())) for i in range(n)]
	dp = [[0,0,0]]
	for i in range(1,n+1):
		temp = []
		temp.append(max(dp[i-1][1], dp[i-1][2]) + abc[i-1][0])
		temp.append(max(dp[i-1][0], dp[i-1][2]) + abc[i-1][1])
		temp.append(max(dp[i-1][1], dp[i-1][0]) + abc[i-1][2])
		dp.append(temp)
	print(max(dp[-1]))

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