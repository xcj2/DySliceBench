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

#import numpy as np

def main():
	ans=0
	n=II()

	for i in range(1,n+1):
		ans+=i*(n+1-i)
	for _ in range(n-1):
		a,b=MI()
		if a>b:
			a,b=b,a
		ans-=a*(n+1-b)
	print(ans)



if __name__ == "__main__":
	main()
