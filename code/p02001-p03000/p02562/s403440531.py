import sys

sys.setrecursionlimit(10**7)
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.G = [[] for _ in range(n)]

    def addEdge(self, f, t, cap, cost):
        # [to, cap, cost, rev]
        self.G[f].append([t, cap, cost, len(self.G[t])])
        self.G[t].append([f, 0, -cost, len(self.G[f])-1])

    def minCostFlow(self, s, t, f):
        n = self.n
        G = self.G
        prevv = [0]*n; preve = [0]*n
        INF = 10**18

        res = 0
        while f:
            dist = [INF]*n
            dist[s] = 0
            update = 1
            while update:
                update = 0
                for v in range(n):
                    if dist[v] == INF:
                        continue
                    gv = G[v]
                    for i in range(len(gv)):
                        to, cap, cost, rev = gv[i]
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost
                            prevv[to] = v; preve[to] = i
                            update = 1
            if dist[t] == INF:
                return -1

            d = f; v = t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]
        return res


N,K = MI()
A = [LI() for _ in range(N)]
max = 10**13

MCF = MinCostFlow(2*N+2)

s,t = 2*N,2*N+1

MCF.addEdge(s,t,N*K,max)

for i in range(N):
    MCF.addEdge(s,i,K,0)
    MCF.addEdge(i+N,t,K,0)
    for j in range(N):
        MCF.addEdge(i,j+N,1,max-A[i][j])

print(N*K*max-MCF.minCostFlow(s,t,N*K))

ANS = [['.']*N for _ in range(N)]

for i in range(N):
    for to,cap,cost,_ in MCF.G[i]:
        if cap == 0 and N <= to < 2*N:
            ANS[i][to-N] = 'X'

for i in range(N):
    print(''.join(ANS[i]))
