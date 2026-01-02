from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,M,P = inpl()
lines = defaultdict(set)

for _ in range(M):
    a,b,c = inpl()
    a,b = a-1,b-1
    lines[a].add((b,-c+P))

#ベルマンフォード(始点と終点が決まってる時)
def BellmanFord(Start,Goal):
    Costs=[INF]*N
    Costs[Start] = 0
    #upd8s = [True]*N
    for i in range(2*N): #2N回ループ(負閉路の検出までみる)
        #will_upd8s = [False]*N
        for s in range(N):
            #if not upd8s[s]: continue    #前回更新してないので見ない
            for t,c in lines[s]:
                if c + Costs[s] < Costs[t]:
                    Costs[t] = Costs[s]+c
                    #will_upd8s[t] = True #更新した点だけ次に見る
                    if i >= N:
                        Costs[t] = -INF

        if i == N-1: #Nループ目のGoalのCostを記録
            tmp = Costs[Goal]

        #upd8s = will_upd8s[:]

    if tmp != Costs[Goal]:
        return -INF
    else:
        return Costs[Goal]

ans = -BellmanFord(0,N-1)
if ans == INF:
    print(-1)
else:
    print(max(0,ans))
