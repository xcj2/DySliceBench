import sys
from collections import defaultdict as dd
from collections import deque
from fractions import Fraction as f
from copy import *
from bisect import *	
from heapq import *
from math import *
from itertools import permutations 
 
def eprint(*args):
    print(*args, file=sys.stderr)
zz=1
 
#sys.setrecursionlimit(10**6)
if zz:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('all.txt','w')
def li():
	return [int(x) for x in input().split()]
def fli():
	return [float(x) for x in input().split()]	
def gi():	
	return [x for x in input().split()]
def fi():
	return int(input())
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())	
def gh():
	sys.stdout.flush()
def graph(n,m):
	for i in range(m):
		x,y=mi()
		a[x].append(y)
		a[y].append(x)
def bo(i):
	return ord(i)-ord('a')
		


tt=1



while tt>0:
	tt-=1
	n=fi()
	a=fli()
	dp=[[0 for i in range(n+1)] for j in range(n+1)]
	for i in range(n):
		if i==0:
			dp[i][0]=1-a[i]
			dp[i][1]=a[i]
		else:
			for j in range(0,n+1):
				dp[i][j]=dp[i-1][j]*(1-a[i])+(dp[i-1][j-1]*a[i] if j>0 else 0)
	ans=0			
	for i in range(n+1):
		if i>n-i:
			ans+=dp[n-1][i]
	print(ans)					
