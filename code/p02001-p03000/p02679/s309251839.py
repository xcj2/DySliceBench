import sys
input = sys.stdin.readline
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

#import numpy as np

from math import gcd
from collections import defaultdict

def main():
	n=II()
	mod=10**9+7

	ans=1
	cnt=0
	d=defaultdict(int)

	for _ in range(n):
		a,b=MI()
		if a==b==0:
			cnt+=1
		elif a==0:
			d[(1,0)]+=1
		elif b==0:
			d[(0,-1)]+=1
		else:
			g=gcd(abs(a),abs(b))
			if a*b>0:
				d[(abs(a//g),abs(b//g))]+=1
			else:
				d[(abs(a//g),-abs(b//g))]+=1


	s=set()

	for a,b in list(d):
		#print(a,b,s)
		if (a,b) in s:
			continue
		if b>=0:
			x=d[(a,b)]
			y=d[(b,-a)]
			s.add((a,b))
			s.add((b,-a))
		else:
			x=d[(a,b)]
			y=d[(-b,a)]
			s.add((a,b))
			s.add((-b,a))
		ans*=2**x+2**y-1
		ans%=mod
	ans+=cnt-1
	print(ans%mod)

if __name__ == "__main__":
	main()
