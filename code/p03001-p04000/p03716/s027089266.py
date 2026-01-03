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

from collections import deque
from heapq import *

def main():
	n=II()
	A=LI()

	X=A[:n]
	Y=[-i for i in A[2*n:]]
	M=A[n:2*n]

	heapify(X)
	heapify(Y)

	xs=sum(X)
	ys=sum(Y)
	XX=[xs]
	YY=[ys]

	for i in M:
		heappush(X,i)
		a=heappop(X)
		xs+=+i-a
		XX.append(xs)

	for i in reversed(M):
		heappush(Y,-i)
		a=heappop(Y)
		ys+=-i-a
		YY.append(ys)

	ans=-10**18

	for i,j in zip(XX,YY[::-1]):
		ans=max(ans,i+j)

	print(ans)
if __name__ == "__main__":
	main()
