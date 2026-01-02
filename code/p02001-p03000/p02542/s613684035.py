from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def addEdge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res

G=MinCostFlow(2502)
n,m=map(int,input().split())
S=[]
for _ in range(n):
    S.append(input())
    
os=0

for i in range(n):
    for q in range(m):
        cnt=i*m+q+1
        now=S[i][q]
        if now=="#":
            continue
        if now=="o":
            G.addEdge(0,cnt,1,0)
            os+=1
        if q<m-1 and S[i][q+1]!="#":
            G.addEdge(cnt,cnt+1,1000,-1)
        if i<n-1 and S[i+1][q]!="#":
            G.addEdge(cnt,cnt+m,1000,-1)
        G.addEdge(cnt,2501,1,0)

ans=G.flow(0,2501,os)
print(-ans)
            