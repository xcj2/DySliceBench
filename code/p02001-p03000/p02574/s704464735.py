import sys
from collections import defaultdict as dd
from collections import deque
from functools import *
from fractions import Fraction as f
from copy import *
from bisect import *	
from heapq import *
from math import *
from itertools import permutations ,product
 
def eprint(*args):
    print(*args, file=sys.stderr)
zz=1
 
#sys.setrecursionlimit(10**6)
if zz:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('all.txt','w')
def inc(d,c):
	d[c]=d[c]+1 if c in d else 1
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
	return 0<=i<n and 0<=j<n	
def bo(i):
	return ord(i)-ord('a')	
def graph(n,m):
	for i in range(m):
		x,y=mi()
		a[x].append(y)
		a[y].append(x)


t=1
N=10**6+5
spf=[i for i in range(N+1)]
for i in range(2,int(ceil(sqrt(N)))+2):
	if spf[i]==i:
		for j in range(i*i,N,i):
			if spf[j]==j:
				spf[j]=i
			
def fact(i):
	s=set()
	while i!=1:
		s.add(spf[i])	
		i//=spf[i]
	return s	

while t>0:
	t-=1
	n=fi()
	a=li()
	s=set()
	g=a[0]
	flag=0
	for i in range(n):
		g=gcd(g,a[i])
		k=fact(a[i])
		if len(s&k)!=0:
			flag|=1
		s|=k
	if flag==0:
		print("pairwise coprime")
	elif g==1:
		print("setwise coprime")	
	else:
		print("not coprime")			
