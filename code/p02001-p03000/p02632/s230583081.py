#import sys
#input = sys.stdin.readline
#input = sys.stdin.buffer.readline


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
from collections import defaultdict

def main():

	mod=10**9+7

	n=II()
	s=input()
	s=len(s)

	pp=[1]
	for i in range(n+10):
		pp.append(pp[-1]*25%mod)


	nn=n+s

	comb=[1]
	for i in range(1,n+10):
		comb.append(comb[-1]*(nn-i+1)*pow(i,mod-2,mod)%mod)
	#print(comb)


	ans=0

	for i in range(n+1):
		ans+=(pp[i]*comb[i])%mod
		ans%=mod
	print(ans)












if __name__ == "__main__":
	main()
