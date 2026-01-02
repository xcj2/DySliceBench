from copy import deepcopy
from sys import exit,setrecursionlimit
import math
from collections import defaultdict,Counter,deque
from fractions import Fraction as frac
import bisect
import sys
input = sys.stdin.readline

setrecursionlimit(1000000)


def main():
	s = input()
	k = int(input())
	s_ = [[s[0],1]]
	ct = 0
	for i in s[1:-1]:
		if(s_[-1][0] == i):
			s_[-1][1] += 1
		else:
			s_.append([i,1])
	for i in s_:
		if(i[1] > 1):
			ct += math.ceil((i[1] - 1)/2)
	ct *= k
	if((len(s) - 1) % 2 == 1 and len(s_ ) == 1):
		print((len(s) - 1) * k // 2)
	elif(s[0] == s[-2] and s_[0][1] == s_[-1][1] and len(s_) != 1):
		print(ct + k - 1)
	else:
		print(ct)


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

def gcd(l):
	x = l.pop()
	y = l.pop()
	while(x%y!=0):
		z = x%y
		x = y
		y = z
	l.append(min(x,y))
	return gcd(l) if len(l) > 1 else l[0]

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
