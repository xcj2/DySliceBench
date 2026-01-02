import sys
sys.setrecursionlimit(10**5+5)
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs():
    q = deque([1])
    while q:
        now = q.popleft()
        for nex,c,w in e[now]:
            if depth[nex]>= 0:
                continue
            depth[nex] = depth[now]+1
            dis[nex] = dis[now]+w
            lca[0][nex] = now
            q.append(nex)

def dfs1(now,p,count1,count2):
    for cou in dcount[now]:
        dcount[now][cou] = count1[cou]
    for wei in dweight[now]:
        dweight[now][wei] = count2[wei]

    for nex,c,w in e[now]:
        if nex == p:
            continue
        count1[c] += 1
        count2[c] += w
        dfs1(nex,now,count1,count2)
        count1[c] -= 1
        count2[c] -= w
n,q = map(int,input().split())
e = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c,d = map(int,input().split())
    e[a].append((b,c,d))
    e[b].append((a,c,d))
size = n+1
bitlen = 19
lca = [[0]*size for i in range(bitlen)]
depth = [-1]*size
dis = [-1]*size
depth[1] = 0
dis[1] = 0

bfs()
for i in range(1,bitlen):
    for j in range(1,size):
        if lca[i-1][j] > 0:
            lca[i][j] = lca[i-1][lca[i-1][j]]
    
def search(x,y):
    dx = depth[x]
    dy = depth[y]
    if dx < dy:
        x,y = y,x
        dx,dy = dy,dx
    dif = dx-dy
    while dif:
        s = dif & (-dif)
        x = lca[s.bit_length()-1][x]
        dif -= s
    if x == y:
        return x
    for i in range(bitlen-1,-1,-1):
        if lca[i][x] != lca[i][y]:
            x = lca[i][x]
            y = lca[i][y]
    return lca[0][x]


Q = [[] for i in range(n+1)]
ans = []
for i in range(q):
    x,y,u,v = map(int,input().split())
    a = search(u,v)
    ans.append(dis[u]+dis[v]-2*dis[a])
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