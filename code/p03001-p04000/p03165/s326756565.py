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
	s=si()
	t=si()
	n=len(s)
	m=len(t)
	dp=[[0 for i in range(m+1)] for j in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,m+1):
			#print(i,j,s[i-1],t[j-1])
			if i==1 and j==1:
					dp[i][j]=int(s[i-1]==t[j-1])
			elif i==1:
				
					dp[i][j]=max([dp[i][j],dp[i][j-1],int(s[i-1]==t[j-1])])
			elif j==1:
				dp[i][j]=max([dp[i][j],dp[i-1][j],int(s[i-1]==t[j-1])])
			else:
				dp[i][j]=max([dp[i][j],dp[i-1][j-1]+int(s[i-1]==t[j-1]),dp[i][j-1],\
					dp[i-1][j]])	
	i=n
	j=m
	ans=""
	tle=0
	#for ii in dp[:n+1]:
	#	print(*ii[:m+1])
	while i>0 or j>0:
		if dp[i][j]==0:
			break
		if i>0 and dp[i-1][j]==dp[i][j]:
			i-=1
		elif j>0 and dp[i][j-1]==dp[i][j]:
			j-=1		
		elif i>0 and j>0 and dp[i][j]-dp[i-1][j-1]==1:
			ans+=s[i-1]
			i-=1
			j-=1
		
		else:
			if i>0 and j>0:
				if dp[i-1][j]>dp[i][j-1]:
					i-=1
				else:
					j-=1	
				
			elif j>0:	
				j-=1
			else:
				i-=1	
		tle+=1
		#print(ans,i,j,tle)
		if tle>n+m:
			break
	if dp[i][j]>0:
		ans+=s[0]			
	print(ans[::-1])		

						
