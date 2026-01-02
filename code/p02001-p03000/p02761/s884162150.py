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
	r=q
	ans=[0]*r.qsize()
	for i in range(r.qsize()-1,-1,-1):
		ans[i] = r.get()
	print(ans)

n, m = map(int, input().split())
s=[]
c=[]
for i in range(m):
	_s, _c = map(int, input().split())
	s.append(_s-1)
	c.append(_c)

if m==0:
	if n==1:
		print(0)
		exit()

ans = -1
for i in range(1000):
	*t, = map(int, list(str(i)))

	if len(t) != n:
		continue

	ok = True
	for j in range(m):
		if t[s[j]]!=c[j]:
			ok = False
			break
 
	if ok:
		print(i)
		quit()

print(-1)