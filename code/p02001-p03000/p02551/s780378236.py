import sys
#from collections import deque
#from functools import *
#from fractions import Fraction as f
from copy import *
from bisect import *	
#from heapq import *
from math import gcd,ceil,sqrt
from itertools import permutations as prm,product
 
def eprint(*args):
    print(*args, file=sys.stderr)
zz=1
 
#sys.setrecursionlimit(10**6)
if zz:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('all.txt','w')
di=[[-1,0],[1,0],[0,1],[0,-1]]
def inc(d,c,x=1):
	d[c]=d[c]+x if c in d else x
def bo(i):
	return ord(i)-ord('A')	
def li():
	return [int(xx) for xx in input().split()]
def fli():
	return [float(x) for x in input().split()]	
def comp(a,b):
	if(a>b):
		return 2
	return 2 if a==b else 0		
def gi():	
	return [xx for xx in input().split()]
def fi():
	return int(input())
def pro(a): 
	return reduce(lambda a,b:a*b,a)		
def swap(a,i,j): 
	a[i],a[j]=a[j],a[i]	
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())			
def gh():
	sys.stdout.flush()
def isvalid(i,j):
	return 0<=i<n and 0<=j<m and a[i][j]!="."
def bo(i):
	return ord(i)-ord('a')	
def graph(n,m):
	for i in range(m):
		x,y=mi()
		a[x].append(y)
		a[y].append(x)

t=1

def updatepoint(point,val,bit):

	while point<=4*n:
		bit[point]+=val
		point+=(point&-point)
def query(point,bit):
	ans=0
	while point>0:
		ans+=bit[point]
		point-=(point&-point)
	return ans	

def update(l,r,val,bit):

	updatepoint(l,val,bit)
	updatepoint(r+1,-val,bit)


while t>0:
	t-=1
	n,q=mi()
	ans=(n-2)**2
	bitc=[0]*(4*n)
	bitr=[0]*(4*n)
	r={}
	c={}
	for i in range(q):
		x,y=mi()
		if x==1 and y not in c:
			c[y]=1
			p=query(y,bitc)
			ans-=(n-1+p)-1
			if n-1+bitr[2]>=y:
				update(2,n-1+bitc[2],y-1-(n-1+bitr[2]),bitr)
		elif x==2 and y not in r:
			r[y]=1
			p=query(y,bitr)
			ans-=(n-1+p)-1
			if n-1+bitc[2]>=y:
				update(2,n-1+bitr[2],y-1-(n-1+bitc[2]),bitc)

	print(ans)			
