class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans

import sys

input=sys.stdin.buffer.readline

N,M=map(int,input().split())
X=int(input())
mod=10**9+7
Edge=[]
EEdge=[]
for i in range(M):
    a,b,c=map(int,input().split())
    Edge.append((c,a-1,b-1))
    EEdge.append((c,a-1,b-1))

Edge.sort()
base=0
edge=[[] for i in range(N)]
uf=UnionFindVerSize(N)
for c,a,b in Edge:
    if not uf.is_same_group(a,b):
        uf.unite(a,b)
        base+=c
        edge[a].append((b,c))
        edge[b].append((a,c))

weight=[0]*N
depth=[0]*N
parent=[0]*N
rmq=[0]*N
def wdfs(v,pv):
    for nv,cost in edge[v]:
        if nv!=pv:
            parent[nv]=v
            depth[nv]=depth[v]+1
            weight[nv]=cost
            rmq[nv]=max(weight[nv],weight[v])
            wdfs(nv,v)

wdfs(0,-1)

LV = (N-1).bit_length()
def construct(prv):
    kprv = [prv]
    S = prv
    for k in range(LV):
        T = [0]*N
        for i in range(N):
            if S[i] is None:
                continue
            T[i] = S[S[i]]
        kprv.append(T)
        S = T
    return kprv

kprv=construct(parent)

def constructkrmq(r):
    krmq=[r]
    S=r
    for k in range(LV):
        T=[0]*N
        for i in range(N):
            if S[i] is None:
                continue
            T[i]=max(S[i],S[kprv[k][i]])
        krmq.append(T)
        S=T
    return krmq


krmq=constructkrmq(rmq)

def lca(u, v):
    dd = depth[v] - depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd

    # assert depth[u] <= depth[v]
    for k in range(LV+1):
        if dd & 1:
            v = kprv[k][v]
        dd >>= 1

    # assert depth[u] == depth[v]
    if u == v:
        return u

    for k in range(LV-1, -1, -1):
        pu = kprv[k][u]; pv = kprv[k][v]
        if pu != pv:
            u = pu; v = pv

    # assert kprv[0][u] == kprv[0][v]
    return kprv[0][u]

def RMQ(u,v):
    #assert depth[u]>depth[v]
    if depth[u]==depth[v]:
        return 0

    num=depth[u]-depth[v]-1
    pos=u
    res=weight[u]
    for i in range(LV-1,-1,-1):
        if num>>i &1==1:
            res=max(res,krmq[i][pos])
            pos=kprv[i][pos]
    return res


up=0
down=0
same=0
for c,u,v in EEdge:
    LCA=lca(u,v)
    minus=max(RMQ(u,LCA),RMQ(v,LCA))
    if base-minus+c>X:
        up+=1
    elif base-minus+c<X:
        down+=1
    else:
        same+=1

if down==0:
    if same==0:
        print(0)
    else:
        ans=pow(2,M,mod)-2*pow(2,up,mod)
        print(ans%mod)
else:
    ans=2*(pow(2,same,mod)-1)*pow(2,up,mod)
    print(ans%mod)
