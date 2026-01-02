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


K = readInt()

q = queue.Queue()

for i in range(1,10):
	q.put(i)

ans = 0
for i in range(K):
	ans = q.get()
	if str(ans)[-1]=="0":
		q.put(int(str(ans)+"0"))
		q.put(int(str(ans)+"1"))
	elif str(ans)[-1]=="9":
		q.put(int(str(ans)+"8"))
		q.put(int(str(ans)+"9"))
	else:
		q.put(int(str(ans)+str(int(str(ans)[-1])-1)))
		q.put(int(str(ans)+str(int(str(ans)[-1]))))
		q.put(int(str(ans)+str(int(str(ans)[-1])+1)))

print(ans)
