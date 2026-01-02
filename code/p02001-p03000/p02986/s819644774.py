import sys
from copy import deepcopy
from operator import add, itemgetter
class Segtree:
    def __init__(self, A, intv, initialize = True, segf = max):
        self.N = len(A)
        self.N0 = 2**(self.N-1).bit_length()
        self.intv = intv
        self.segf = segf
        if initialize:
            self.data = [intv]*self.N0 + A + [intv]*(self.N0 - self.N)
            for i in range(self.N0-1, 0, -1):
                self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
        else:
            self.data = [intv]*(2*self.N0)
        
    def update(self, k, x):
        k += self.N0
        self.data[k] = x
        while k > 0 :
            k = k >> 1
            self.data[k] = self.segf(self.data[2*k], self.data[2*k+1])
    
    def query(self, l, r):
        L, R = l+self.N0, r+self.N0
        s = self.intv
        while L < R:
            if R & 1:
                R -= 1
                s = self.segf(s, self.data[R])
            if L & 1:
                s = self.segf(s, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return s

def getpar(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = None
    stack = [p]
    visited = set([p])
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            stack.append(vf)
    return par

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res

def eulertour(Par, Cld, st):
    #P[par]にはNoneをいれる
    Cld = deepcopy(Cld)
    N = len(Cld)
    St = [None]*N
    En = [None]*N
    et = []
    sign = []
    vf = st
    cnt = 0
    depth = [0]*N
    while vf is not None:
        vn = vf
        et.append(vn)
        if St[vn] is None:
            St[vn] = cnt
        En[vn] = cnt
        cnt += 1
        if Cld[vn]:
            vf = Cld[vn].pop()
            sign.append(1)
            depth[vf] = depth[vn] + 1
        else:
            vf = P[vn]
            sign.append(-1)
    return St, En, et, sign[:-1], depth

N, Q = map(int, input().split())
Edge = [[] for _ in range(N)]
Edgelen = [0]*(N-1)
Edgenum = {}
Color = [[] for _ in range(N)]
for i in range(N-1):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
    Edgelen[i] = d
    Edgenum[(a, b)] = i
    Edgenum[(b, a)] = i
    Color[c].append(i) 

P = getpar(Edge, 0)
C = getcld(P)
St, En, et, sign, depth = eulertour(P, C, 0)
etnum = [Edgenum[(v1, v2)] for v1, v2 in zip(et, et[1:])]
etnuminv = [[] for _ in range(N-1)]
for i, e in enumerate(etnum):
    etnuminv[e].append(i)
etl = [Edgelen[num]*sign[i] for i, num in enumerate(etnum)]

LCA = Segtree(et, None, initialize = True, segf = lambda x, y: x if y is None or (x is not None and depth[x] < depth[y]) else y)
Leng = Segtree([0]+etl, 0, initialize = True, segf = add)

Query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]
Ans = [None]*Q
CQ = [[] for _ in range(N)]
for i, (x, y, u, v) in enumerate(Query):
    CQ[x].append((i, y, u-1, v-1))

for col, cq in enumerate(CQ):
    if not cq:
        continue
    inf = 2*10**9
    for vidx in Color[col]:
        Leng.update(1+etnuminv[vidx][0], inf)
        Leng.update(1+etnuminv[vidx][1], -inf)
    
    for i, y, u, v in cq:
        if St[u] > St[v]:
            u, v = v, u
        su = St[u]
        sv = St[v]
        lca = LCA.query(su, sv+1)
        dis = Leng.query(0, su+1) + Leng.query(0,sv+1) - 2*Leng.query(0,St[lca]+1)
        disq, disr = divmod(dis, inf)
        Ans[i] = disr + disq*y
    for vidx in Color[col]:
        Leng.update(1+etnuminv[vidx][0], Edgelen[vidx])
        Leng.update(1+etnuminv[vidx][1], -Edgelen[vidx])
print('\n'.join(map(str, Ans)))
