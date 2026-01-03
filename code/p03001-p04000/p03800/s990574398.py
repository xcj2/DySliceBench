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
from itertools import combinations

def main():
	n=II()
	s=input().decode()


	def check(a,b,c):
		A=[None]*(n+1)
		A[0]=a
		A[1]=b
		A[n-1]=c
		A[n]=a

		for i in range(1,n):
			if (s[i]=="o" and A[i]=="S") or (s[i]=="x" and A[i]=="W"):
				if A[i+1]==None:
					A[i+1]=A[i-1]
				else:
					if A[i+1]!=A[i-1]:
						return
			#if (s[i]=="o" and A[i]=="W") or (s[i]=="x" and A[i]=="S"):
			else:
				if A[i+1]==None:
					if A[i-1]=="S":
						A[i+1]="W"
					else:
						A[i+1]="S"
				else:
					if A[i+1]==A[i-1]:
						return

		print(*A[:-1],sep="")
		exit(0)

	if s[0]=="o":
		check("S","S","S")
		check("S","W","W")
		check("W","W","S")
		check("W","S","W")

	else:
		check("S","S","W")
		check("S","W","S")
		check("W","S","S")
		check("W","W","W")

	print(-1)













if __name__ == "__main__":
	main()
