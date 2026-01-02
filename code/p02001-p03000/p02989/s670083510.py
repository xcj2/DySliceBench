from copy import *
from sys import *
import math
import queue
from collections import defaultdict,Counter,deque
from fractions import Fraction as frac

setrecursionlimit(1000000)

#s[i] is linked with t[len(s)-i-1]
def main():
	n = int(input())
	d = list(map(int,input().split()))
	d.sort()
	print(max(d[n//2] - d[n//2-1],0))


def zip(a):
	mae = a[0]
	ziparray = [mae]
	for i in range(1,len(a)):
		if(mae != a[i]):
			ziparray.append(a[i])
			mae = a[i]
	return ziparray

def is_prime(n):
	if n < 2: return False

	for k in range(2, int(math.sqrt(n)) + 1):
		if n % k == 0:
			return False

	return True

def list_replace(n,f,t):
	return [t if i==f else i for i in n]

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
	def __init__(self):
		self.q = deque([])
	def push(self,i):
		self.q.append(i)
	def pop(self):
		return self.q.popleft()
	def size(self):
		return len(self.q)
	def debug(self):
		return self.q

class Stack():
	def __init__(self):
		self.q = []
	def push(self,i):
		self.q.append(i)
	def pop(self):
		return self.q.pop()
	def size(self):
		return len(self.q)
	def debug(self):
		return self.q

class graph():
	def __init__(self):
		self.graph = defaultdict(list)
	def addnode(self,l):
		f,t = l[0],l[1]
		self.graph[f].append(t)
		self.graph[t].append(f)
	def rmnode(self,l):
		f,t = l[0],l[1]
		self.graph[f].remove(t)
		self.graph[t].remove(f)
	def linked(self,f):
		return self.graph[f]

class dgraph():
	def __init__(self):
		self.graph = defaultdict(set)
	def addnode(self,l):
		f,t = l[0],l[1]
		self.graph[f].append(t)
	def rmnode(self,l):
		f,t = l[0],l[1]
		self.graph[f].remove(t)
	def linked(self,f):
		return self.graph[f]

main()