import sys
from bisect import *
from collections import deque
pl=1
#from math import *
from copy import *
#sys.setrecursionlimit(10**6)
if pl:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('outpt.txt','w')

def li():
	return [int(xxx) for xxx in input().split()]
def fi():
	return int(input())
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())	

def find(i):
	if i==a[i]:
		return i
	a[i]=find(a[i])
	return a[i]
def union(x,y):
	xs=find(x)
	ys=find(y)
	if xs!=ys:
		if rank[xs]<rank[ys]:
			xs,ys=ys,xs
		rank[xs]+=1
		a[ys]=xs		
t=1
while t>0:
	t-=1
	n,m=mi()
	a=[i for i in range(n+1)]	
	rank=[0 for i in range(n+1)]			
	for i in range(m):
		x,y=mi()
		union(x,y) 
	s=set()	
	for i in range(1,n+1):
		a[i]=find(i)
		s.add(a[i])
	print(len(s)-1)	


