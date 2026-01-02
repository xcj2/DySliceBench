import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	N,M,L = MI()
	to = [[] for _ in range(N)]
	dist = [[float("inf") for _ in range(N)] for _ in range(N)]

	def warshall_floyd(N):
		for mid in range(N):
			for s in range(N):
				for g in range(s+1,N):
					dist[s][g] = min(dist[s][g], dist[s][mid]+dist[mid][g])
					dist[g][s] = dist[s][g]


	for _ in range(M):
		a,b,c = MI()
		dist[a-1][b-1],dist[b-1][a-1]=c,c
	for i in range(N):
		dist[i][i] = 0

	warshall_floyd(N)

	for i in range(N):
		for j in range(i+1,N):
			if dist[i][j]<=L :
				dist[i][j],dist[j][i]=1,1
			else:
				dist[i][j],dist[j][i]=float("inf"),float("inf")

	warshall_floyd(N)

	Q = II()
	for _ in range(Q):
		s,t = MI()
		ans = dist[s-1][t-1]-1
		if(ans == float("inf")):
			print(-1)
		else:
			print(ans)

main()