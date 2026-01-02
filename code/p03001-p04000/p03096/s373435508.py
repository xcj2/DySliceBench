import sys
read = sys.stdin.buffer.read
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
# rstrip().decode('utf-8')

#import numpy as np

def main():
	n=II()
	C=[]
	pre=0
	for i in range(n):
		a=II()
		if a!=pre:
			C.append(a)
		pre=a
	#print(C)

	n=len(C)
	dp=[0]*(n+1)
	dp[1]=1
	li=[0]*(max(C)+10)
	li[C[0]]=1

	for i in range(1,n):
		#print(dp)
		#print(li)
		dp[i+1]=(dp[i]+dp[li[C[i]]])%(10**9+7)
		li[C[i]]=i+1
	print(dp[-1])


if __name__ == "__main__":
	main()
