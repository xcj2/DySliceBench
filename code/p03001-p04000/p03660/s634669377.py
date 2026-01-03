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

def main():
	n=II()
	G=[[] for _ in range(n+1)]

	for _ in range(n-1):
		a,b=MI()
		G[a].append(b)
		G[b].append(a)
	#print(G)


	B=[-1]*(n+1)
	W=[-1]*(n+1)
	B[1]=0
	W[n]=0

	Q=deque([1])
	while Q:
		now=Q.popleft()
		for i in G[now]:
			if B[i]==-1:
				B[i]=B[now]+1
				Q.append(i)
	#print(B)

	Q=deque([n])
	while Q:
		now=Q.popleft()
		for i in G[now]:
			if W[i]==-1:
				W[i]=W[now]+1
				Q.append(i)
	#print(W)

	s=0
	f=0
	for i,j in zip(B[1:],W[1:]):
		if i<=j:
			f+=1
		else:
			s+=1
	#print(f,s)

	print("Fennec" if f>s else "Snuke")






if __name__ == "__main__":
	main()
