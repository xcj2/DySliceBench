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

#ベルマンフォード(始点と終点が決まってる時)
def BellmanFord(Start,Goal):
	Costs=[INF]*N
	Costs[Start] = 0
	upd8s = [True]*N
	for i in range(2*N): #2N回ループ(負回路の検出までみる)
		will_upd8s = [False]*N
		upd8 = False
		for s in range(N):
			if not upd8s[s]: continue	#前回更新してないので見ない
			for t,c in lines[s]:
				if c + Costs[s] < Costs[t]:
					Costs[t] = Costs[s]+c
					upd8 = True
					will_upd8s[t] = True #更新した点だけ次に見る

		if not upd8: #なにも更新しなかったら終わり
			return Costs[Goal]

		if i == N-1: #Nループ目のGoalのCostを記録
			tmp = Costs[Goal]

		upd8s = will_upd8s[:]

	if tmp != Costs[Goal]:
		return -INF
	else:
		return Costs[Goal]

print(-BellmanFord(0,N-1))
