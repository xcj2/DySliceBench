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
from collections import deque

def main():
	n=II()
	G=[]
	for i in range(n):
		G.append(list(map(int,input())))
		#print(G)

	ans=0
	for i in range(n):
		v=[-2]*n
		v[i]=0
		q=deque()
		q.append([i,0])

		while q:
			now,d=q.popleft()
			for j in range(n):
				if G[now][j]==1:
					if v[j]==-2:
						v[j]=d+1
						q.append([j,d+1])
					elif v[j]==d-1 or v[j]==d+1:
						continue
					else:
						print(-1)
						exit(0)
		ans=max(ans,max(v)+1)


	print(ans)

if __name__ == "__main__":
	main()
