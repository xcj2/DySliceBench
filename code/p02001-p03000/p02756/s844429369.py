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

s = readChar()
q = readInt()
qa = []
booh = 0
for i in range(q):
	x = input()
	if x=="1":
		qa.append([1,0,0])
	else:
		x = x.split()
		qa.append([int(x[0]),int(x[1]),x[2]])

def t1(s):
	return s[::-1]

def t2(f,c,s):
	if f==1:
		return c+s
	else:
		return s+c

fi=""
la=""
q = queue.deque()
for a in qa:
	if a[0]==1:
		booh = (booh+1)%2
	else:
		if (a[1]+booh)%2==1:
			fi=a[2]+fi
			q.appendleft(a[2])
		else:
			la+=a[2]

s = "".join(list(q))+s+la
if booh==1:
	s = t1(s)

print(s)