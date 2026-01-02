import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

#import numpy as np
import bisect
from collections import deque

def main():
	n=II()
	A=[II() for _ in range(n)]

	Q=deque([A[0]])
	#print(Q)
	for i in range(1,n):
		if A[i]<=Q[0]:
			Q.appendleft(A[i])
		else:
			a=bisect.bisect_left(Q,A[i])
			Q[a-1]=A[i]
	print(len(Q))








if __name__ == "__main__":
	main()