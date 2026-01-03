INF = 10**10
N,M=map(int,input().split())
e=[]
w=[[INF for j in range(N)]for i in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    w[a-1][b-1]=c
    w[b-1][a-1]=c
    e.append((a-1,b-1,c))

class lheapq():
#最小値を取り出す優先度付きキュー
    def __init__(self,p):
        self.l = []
        if p:
            for sp in p:
                self.heappush(sp)

    def heappush(self,a):
        n=len(self.l)
        self.l.append(a)
        t = n
        while t != 0:
            if self.l[t][1] < self.l[(t-1)//2][1]:
                self.l[t],self.l[(t-1)//2] = self.l[(t-1)//2],self.l[t]
                t = (t-1)//2
            else:break

    def heappop(self):
        n=len(self.l)
        if n == 0:
            return (-1,0)
        if n == 1:
            return self.l.pop()
        ret = self.l[0]
        self.l[0] = self.l.pop()
        n -= 1
        t = 0
        while t<n:
            child1 = t*2+1
            child2 = t*2+2
            if child1 >= n:
                break
            elif child2 >= n:
                if self.l[t][1] > self.l[child1][1]:
                    self.l[t],self.l[child1] = self.l[child1],self.l[t]
                    t = child1
                else:break
            else:
                if self.l[child2][1] < self.l[child1][1]:
                    child1,child2 = child2,child1
                if self.l[t][1] > self.l[child1][1]:
                    self.l[t],self.l[child1] = self.l[child1],self.l[t]
                    t = child1
                elif self.l[t][1] > self.l[child2][1]:
                    self.l[t],self.l[child2] = self.l[child2],self.l[t]
                    t = child2
                else:break
        return ret
    
    def isnotblank(self):
        if self.l:return True
        else:return False

def dijkstra(s,g,N,e):
    INF =10**10
    res = [INF for _ in range(N)]
    q=lheapq([(s,0)])
    while q.isnotblank():
        while q.isnotblank():
            des,dis = q.heappop()
            if res[des] == INF:
                res[des] = dis
                break
        for se in e[des]:
            if res[se[0]] == INF:
                q.heappush((se[0],se[1]+res[des]))
    return res[g]

for k in range(N):
    for i in range(N):
        for j in range(N):
            w[i][j] = min(w[i][j],w[i][k]+w[k][j])

res = 0
for i in range(M):
    g=[[] for _ in range(N)]
    for j in range(M):
        if j!=i:
            a,b,c = e[j][0],e[j][1],e[j][2]
            g[a].append((b,c))
            g[b].append((a,c))
    a,b,c = e[i][0],e[i][1],e[i][2]
    if c != w[a][b] and dijkstra(a,b,N,g) == w[a][b]:
        res += 1

print(res)