import sys

input=sys.stdin.buffer.readline


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


def main():
	n,m,p=MI()
	G=[[] for _ in range(n+1)]
	
	for _ in range(m):
		a,b,c=MI()
		G[a].append([b,c-p])
	#print(G)
	
	coin=[-10**18]*(n+1)
	coin[1]=0
	
	for _ in range(n):
		for i in range(1,n+1):
			for b,c in G[i]:
				coin[b]=max(coin[b],coin[i]+c)
	#print(coin)
	ans=coin[-1]
	
	check=[False]*(n+1)
	for i in range(1,n+1):
		for b,c in G[i]:
			if coin[b]<coin[i]+c and coin[b]>-10**10:
				check[b]=True
	
	for _ in range(n):
		for i in range(1,n+1):
			for b,c in G[i]:
				check[b]=check[i] or check[b]
	#print(check)
	
	if check[n]==True:
		ans=-1
	else:
		ans=max(ans,0)
	
	print(ans)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

if __name__=="__main__":
	main()
