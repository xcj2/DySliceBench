import sys
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

def main():

	n=II()
	A=LI()

	if A[-1]!=2:
		print(-1)
		exit()

	l=2
	r=2

	for i in range(n-2,-1,-1):
		l=((l-1)//A[i]+1)*A[i]
		r=((r+A[i+1]-1)//A[i])*A[i]
		if l>r:
			print(-1)
			exit()

	print(l,r+A[0]-1)
















if __name__ == "__main__":
	main()
