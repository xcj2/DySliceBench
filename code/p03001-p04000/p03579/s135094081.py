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
	n,m=MI()

	G=[[] for _ in range(n+1)]

	for _ in range(m):
		a,b=MI()
		G[a].append(b)
		G[b].append(a)
	#print(G)

	D=[-1]*(n+1)


	Q=deque()
	Q.append([1,0])

	#print(Q)

	f=0

	while Q:
		#print(Q)
		now,d=Q.pop()
		D[now]=d
		for nx in G[now]:
			if D[nx]==-1:
				Q.append([nx,1-d])
			elif D[nx]!=d:
				continue
			else:
				f=1
				break


	if f==1:
		ans=(n*(n-1))//2
	else:
		ans=D.count(0)*D.count(1)


	ans-=m

	print(ans)

















if __name__ == "__main__":
	main()
