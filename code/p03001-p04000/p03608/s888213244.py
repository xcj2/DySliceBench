import sys
read = sys.stdin.buffer.read
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
# rstrip().decode('utf-8')

from itertools import permutations

def main():
	n,m,R=MI()
	r=LI()

	G=[[10**9]*(n+1) for _ in range(n+1)]
	for i in range(n+1):
		G[i][i]=0



	for _ in range(m):
		a,b,c=MI()
		G[a][b]=min(G[a][b],c)
		G[b][a]=min(G[b][a],c)
	#print(G)

	for k in range(n+1):
		for i in range(n+1):
			for j in range(n+1):
				G[i][j]=min(G[i][j],G[i][k]+G[k][j])
	#print(G)

	ans=10**9
	for i in permutations(r,R):
		#print(i)
		ret=0
		for j in range(R-1):
			ret+=G[i[j]][i[j+1]]
		#print(ret)
		ans=min(ans,ret)
	print(ans)





if __name__ == "__main__":
	main()
