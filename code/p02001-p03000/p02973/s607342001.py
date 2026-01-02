import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

import bisect
from collections import deque

def main():
	n=II()
	A=[II() for _ in range(n)]

	Q=deque()
	Q.append(A[0])

	for i in A[1:]:
		x=bisect.bisect_left(Q,i)
		if x==0:
			Q.appendleft(i)
		else:
			Q[x-1]=i
	print(len(Q))





















if __name__ == "__main__":
	main()
