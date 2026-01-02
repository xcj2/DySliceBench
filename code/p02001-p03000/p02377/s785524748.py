import heapq

class edge:
    def __init__(self, to, cap, cost, rev):
        self.to: int = to
        self.cap: int = cap
        self.cost: int = cost
        self.rev: int = rev


class min_cost_flow:
    def __init__(self, N):
        self.N: int = N
        self.INF: int = 1000000000000000000
        self.G = [[] for i in range(N)]
        
    def add_edge(self, fro, to, cap, cost):
        self.G[fro].append(edge(to, cap, int(cost), int(len(self.G[to]))))
        self.G[to].append(edge(fro, 0, -int(cost), int(len(self.G[fro]) - 1)))
        
    def solve(self, s, t, f):
        N = self.N
        prevv = [0 for i in range(N)]
        preve = [0 for i in range(N)]
        
        ret = 0
        while 0 < f:
            dist = [self.INF for i in range(N)]
            dist[s] = 0
            hq = [(0, s)]
            heapq.heapify(hq)
            while hq:
                d, v = heapq.heappop(hq)
                for i in range(len(self.G[v])):
                    e = self.G[v][i]
                    if 0 < e.cap and dist[v] + e.cost < dist[e.to]:
                        dist[e.to] = dist[v] + e.cost
                        prevv[e.to] = v
                        preve[e.to] = i
                        heapq.heappush(hq, (dist[e.to], e.to))

            # 流せない
            if dist[t] == self.INF:
                return self.INF

            d = f
            v = t
            while v != s:
                d = min(d, self.G[prevv[v]][preve[v]].cap)
                v = prevv[v]

            f -= d
            ret += d * dist[t]
            v = t
            while v != s:
                e = self.G[prevv[v]][preve[v]]
                e.cap -= d
                self.G[v][e.rev].cap += d
                v = prevv[v]
    
        return ret

# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B
v, e, f = map(int, input().split())
mcf = min_cost_flow(v)
for i in range(e):
    ui, vi, ci, di = map(int, input().split())
    mcf.add_edge(ui, vi, ci, di)
    
ans = mcf.solve(0, v-1, f)
if ans == mcf.INF:
    print(-1)
else:
    print(ans)
