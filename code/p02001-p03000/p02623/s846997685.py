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
import bisect

def main():
	n,m,k=MI()
	A=LI()
	B=LI()

	for i in range(1,n):
		A[i]+=A[i-1]
	for j in range(1,m):
		B[j]+=B[j-1]
	#print(A,B)

	ans=bisect.bisect_right(B,k)

	for i in range(n):
		if k>=A[i]:
			kk=k-A[i]
			j=bisect.bisect_right(B,kk)
			#print(kk,i,j)
			ans=max(ans,i+j+1)
		else:
			break

	print(ans)


if __name__ == "__main__":
	main()
