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
	n=II()
	A=LI()
	A.sort(reverse=True)

	ans=A[0]
	ans+=2*sum(A[1:(n+1)//2-1])

	if n%2:
		ans+=A[n//2]
	elif n>3:
		ans+=2*A[(n-1)//2]

	print(ans)











if __name__ == "__main__":
	main()
