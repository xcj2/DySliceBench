import sys
sys.setrecursionlimit(10**5+5)
from collections import defaultdict,deque
input = sys.stdin.readline
class LCA:

    def __init__(self,n):
        self.size = n+1
        self.bitlen = n.bit_length()
        self.lca = [[0]*self.size for i in range(self.bitlen)]
        self.depth = [-1]*self.size
        self.dis = [-1]*self.size
        self.depth[1] = 0
        self.dis[1] = 0
    def make(self,root):
        q = deque([root])
        while q:
            now = q.popleft()
            for nex,c,w in e[now]:
                if self.depth[nex]>= 0:
                    continue
                self.depth[nex] = self.depth[now]+1
                self.dis[nex] = self.dis[now]+w
                self.lca[0][nex] = now
                q.append(nex)
        for i in range(1,self.bitlen):
            for j in range(self.size):
                if self.lca[i-1][j] > 0:
                    self.lca[i][j] = self.lca[i-1][self.lca[i-1][j]]
    
    def search(self,x,y):
        dx = self.depth[x]
        dy = self.depth[y]
        if dx < dy:
            x,y = y,x
            dx,dy = dy,dx
        dif = dx-dy
        while dif:
            s = dif & (-dif)
            x = self.lca[s.bit_length()-1][x]
            dif -= s
        if x == y:
            return x
        for i in range(self.bitlen-1,-1,-1):
            if self.lca[i][x] != self.lca[i][y]:
                x = self.lca[i][x]
                y = self.lca[i][y]
        
        return self.lca[0][x]

n,q = map(int,input().split())
e = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c,d = map(int,input().split())
    e[a].append((b,c,d))
    e[b].append((a,c,d))
    
lca = LCA(n)
lca.make(1)

Q = [[] for i in range(n+1)]
ans = []
for i in range(q):
    x,y,u,v = map(int,input().split())
    a = lca.search(u,v)
    ans.append(lca.dis[u]+lca.dis[v]-2*lca.dis[a])
    Q[u].append((x,y,i,1))
    Q[v].append((x,y,i,1))
    Q[a].append((x,y,i,-2))


count = defaultdict(int)
weight = defaultdict(int)
def dfs1(now,p):
    for x,y,ind,z in Q[now]:
        ans[ind] += z*(y*count[x]-weight[x])
    for nex,c,w in e[now]:
        if nex == p:
            continue
        count[c] += 1
        weight[c] += w
        dfs1(nex,now)
        count[c] -= 1
        weight[c] -= w
    
dfs1(1,0)

for i in ans:
    print(i)