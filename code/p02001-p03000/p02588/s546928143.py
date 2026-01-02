import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

import math
from collections import defaultdict

def main():
	n=II()
	#A=[]
	#B=[]
	d=defaultdict(int)

	for _ in range(n):
		x=float(input())
		x*=10**9
		x=int(x+0.5)
		g=math.gcd(x,10**9)
		#print(g)
		a=math.gcd(x//g,10**9)
		b=10**9//g
		#A.append(math.gcd(x//g,10**9))
		#B.append(10**9//g)
		d[(a,b)]+=1
	#print(A,B,d)

	ans=0

	for k,v in d.items():
		for kk,vv in d.items():
			if k!=kk:
				if (k[0]*kk[0])%(k[1]*kk[1])==0:
					#print(k,v,kk,vv)
					ans+=v*vv


	ans//=2

	for k,v in d.items():
		if k[1]==1:
			ans+=v*(v-1)//2

	print(ans)





















if __name__ == "__main__":
	main()
