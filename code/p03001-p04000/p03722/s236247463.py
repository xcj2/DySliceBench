from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N,M = inpl()
lines = defaultdict(set)

for _ in range(M):
	a,b,c = inpl()
	a,b = a-1,b-1
	lines[a].add((b,-c))

def BellmanFord(Start,Goal):
	Costs=[INF]*N
	Costs[Start] = 0
	upd8s = [True]*N
	for i in range(N): #N回ループ(高々N-1回で収束する)
		#will_upd8s = [False]*N
		upd8 = False
		for s in range(N):
			#if not upd8s[i]: continue	#前回更新してないので見ない
			for t,c in lines[s]:
				if c + Costs[s] < Costs[t]:
					Costs[t] = Costs[s]+c
					upd8 = True
					#will_upd8s[t] = True #更新した点だけ次に見る

		#upd8s = will_upd8s[:]
		if not upd8:
			return Costs[Goal] #なにも更新しなかったら終わり
	else: #負回路の検出(もうN回)
		pc = Costs[Goal]
		for i in range(N):
			upd8 = True
			for s in range(N):
				for t,c in lines[s]:
					if c + Costs[s] < Costs[t]:
						Costs[t] = Costs[s]+c
						upd8 = True
			if not upd8: break

		if pc != Costs[Goal]:
			return -INF
		else:
			return Costs[Goal]

print(-BellmanFord(0,N-1))
