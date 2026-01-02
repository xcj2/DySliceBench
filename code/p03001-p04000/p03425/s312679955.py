from copy import deepcopy
from sys import exit,setrecursionlimit
import math
from collections import defaultdict,Counter,deque
from fractions import Fraction as frac
import fractions
from functools import reduce
from operator import mul
import bisect
import sys
import logging
import heapq
import itertools

#logging.basicConfig(level=logging.DEBUG)

input = sys.stdin.readline

setrecursionlimit(1000000)


def main():
	n = int(input())
	s = defaultdict(set)
	for _ in range(n):
		t = input()
		if(t[0] in ['M','A','R','C','H']):
			s[t[0]].add(t)
	s = list(s.values())
	ans = 0
	for i in itertools.permutations(s,3):
		ans += len(i[0]) * len(i[1]) * len(i[2])
	print(ans//6)

def factorization(n):
	arr = []
	temp = n
	for i in range(2, int(-(-n**0.5//1))+1):
		if temp%i==0:
			cnt=0
			while temp%i==0:
				cnt+=1
				temp //= i
			arr.append([i, cnt])

	if temp!=1:
		arr.append([temp, 1])

	if arr==[]:
		arr.append([n, 1])

	return arr

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

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

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

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

class PriorityQueue():
	def __init__(self):
		self.queue = []
	def push(self,i):
		heapq.heappush(self.queue,-i)
	def pop(self):
		return -1 * heapq.heappop(self.queue)
	def sum(self):
		return -sum(self.queue)

main()
