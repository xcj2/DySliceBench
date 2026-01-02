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


def main():
	a,b,c,d=MI()
	dp=[[0]*(d+1) for _ in range(c+1)]
	dp[a][b]=1

	for i in range(a-1,c):
		for j in range(b-1,d):
			if i+1==a and j+1==b:
				continue
			#print(i,j)
			dp[i+1][j+1]=dp[i][j+1]*(j+1)+dp[i+1][j]*(i+1)-i*j*dp[i][j]
			dp[i+1][j+1]%=998244353

	print(dp[c][d])
















if __name__ == "__main__":
	main()
