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

from collections import deque

def main():
	n,m=MI()

	G=[[] for _ in range(n+1)]

	for _ in range(m):
		a,b=MI()
		G[a].append(b)
		G[b].append(a)

	ans=[0]*(n+1)

	Q=deque([1])
	sumi=set()

	while Q:
		now=Q.popleft()

		for next in G[now]:
			if next in sumi:
				continue
			else:
				Q.append(next)
				ans[next]=now
				sumi.add(next)

	print("Yes")

	print(*ans[2:],sep="\n")






































if __name__ == "__main__":
	main()
