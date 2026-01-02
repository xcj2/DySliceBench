import math
import queue
from collections import defaultdict
 
def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()
def factorization(n):
	res = []
	if n%2==0:
		res.append(2)
	for i in range(3,math.floor(n//2)+1,2):
		if n%i==0:
			c = 0
			for j in res:
				if i%j==0:
					c=1
			if c==0:
				res.append(i)
	return res
def fact2(n):
	p = factorization(n)
	res = []
	for i in p:
		c=0
		z=n
		while 1:
			if z%i==0:
				c+=1
				z/=i
			else:
				break
		res.append([i,c])
	return res
def fact(n):#階乗
	ans = 1
	m=n
	for _i in range(n-1):
		ans*=m
		m-=1
	return ans
def comb(n,r):#コンビネーション
	if n<r:
		return 0
	l = min(r,n-r)
	m=n
	u=1
	for _i in range(l):
		u*=m
		m-=1
	return u//fact(l)
def printQueue(q):
	r=qb
	ans=[0]*r.qsize()
	for i in range(r.qsize()-1,-1,-1):
		ans[i] = r.get()
	print(ans)
def dq():
	return queue.deque()
class UnionFind():
	def __init__(self, n):
		self.n = n
		self.parents = [-1]*n

	def find(self, x): # root
		if self.parents[x]<0:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]

	def union(self,x,y):
		x = self.find(x)
		y = self.find(y)

		if x==y:
			return

		if self.parents[x]>self.parents[y]:
			x,y = y,x

		self.parents[x]+=self.parents[y]
		self.parents[y]=x

	def size(self,x):
		return -1*self.parents[self.find(x)]

	def same(self,x,y):
		return self.find(x)==self.find(y)

	def members(self,x): # much time
		root = self.find(x)
		return [i for i in range(self.n) if self.find(i)==root]

	def roots(self):
		return [i for i,x in enumerate(self.parents) if x<0]

	def group_count(self):
		return len(self.roots())

	def all_group_members(self):
		return {r: self.members(r) for r in self.roots()} # 1~n
def bitArr(n):#ビット全探索
	x = 1
	zero = "0"*n
	ans = []
	ans.append([0]*n)
	for i in range(2**n-1):
		ans.append(list(map(lambda x:int(x),list((zero+bin(x)[2:])[-1*n:]))))
		x+=1
	return ans;
def arrsSum(a1,a2):
	for i in range(len(a1)):
		a1[i]+=a2[i]
	return a1

def maxValue(a,b,v):
	v2 = v
	for i in range(v2,-1,-1):
		for j in range(v2//a+1): #j:aの個数
			k = i-a*j
			if k%b==0:
				#print(j,k//b)
				return i
	return -1

a,b,c,d,e,f = readInts()

waVa = maxValue(a*100,b*100,f)
suVa = maxValue(c,d,min(f-waVa,waVa*e//100))
maxR = 0

anw = waVa
ans = suVa

while 1:
	waVa = maxValue(a*100,b*100,waVa-1)
	suVa = maxValue(c,d,min(f-waVa,waVa*e//100))
	if waVa<0 or suVa<0:
		continue
	if waVa == 0:
		break
	if maxR<100*suVa/(suVa+waVa):
		maxR = 100*suVa/(suVa+waVa)
		anw = waVa
		ans = suVa

print(anw+ans,ans)