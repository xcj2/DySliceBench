import sys
from collections import defaultdict
readline = sys.stdin.readline
N, Q = map(int, readline().split())

class SegTree:
    def __init__(self, init_val, n, ide_ele, seg_func):
        self.segfunc = seg_func
        self.num = 2**(n-1).bit_length()
        self.ide_ele = ide_ele
        self.seg=[self.ide_ele]*2*self.num
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]    
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k+1:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
        
    def query(self, p, q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

def bsearch(ll, target, min_i, max_i):
    # l[index] <= target < l[index+1] となるindexを返す
    if ll[max_i] <= target:
        return max_i
    if target < ll[min_i]:
        return None
    index = len(ll)//2
    while True:
        if ll[index] <= target:
            if target < ll[index+1]:
                return index
            index, min_i = (index+1 + max_i)//2, index+1
            continue
        index, max_i = (index-1 + min_i)//2, index-1

def process():

    G = [[] for _ in range(N+1)]
    dp = {}
    for v in range(N-1):
        a, b, c, d = map(int, readline().split())
        G[a].append(b)
        G[b].append(a)
        dp[(min(a,b), max(a,b))] = c, d

    S = [1]*(2*N+1)
    F = [0]*(N+1)
    stack = []
    for u in G[1]:
        stack += [-1, u]

    visited = set([1])
    depth, depthh = [0]*(N+1), [0]*(N+1)
    mmn = [[0] for _ in range(N)]
    msn = [[0] for _ in range(N)]
    iin = [[0] for _ in range(N)]
    path = [1]
    ii = 0

    while True:
        if len(stack) == 0:
            break
        v = stack.pop()
        ii += 1
        if v > 0:
            visited.add(v)
            parent = path[-1]
            path.append(v)
            #print(parent)

            cc, dpd = dp[(min(v,parent), max(v,parent))]
            F[v], S[ii] = ii, v
            depth[v], depthh[v] = depth[parent] + 1, depthh[parent] + dpd

            mmn[cc].append(mmn[cc][-1]+1)
            msn[cc].append(msn[cc][-1]+dpd)
            iin[cc].append(ii)

            for u in G[v]:
                if u in visited:
                    continue
                stack += [-v, u]
        else:
            child = path.pop()
            cc, dpd = dp[(min(-v, child), max(-v, child))]
            S[ii] = v
            mmn[cc].append(mmn[cc][-1]-1)
            iin[cc].append(ii)
            msn[cc].append(msn[cc][-1]-dpd)
    # オイラーツアー
#    print(S)
#    print(depth)
#    print(F)
#    print(iin)
    stree = SegTree([(depth[abs(v)], i) for i, v in enumerate(S)], len(S), (N, None), min)

    for q in range(Q):
        x, y, u, v = map(int, readline().split())
        fu = F[u]; fv = F[v]
        if fu > fv:
            fu, fv = fv, fu

        cc = abs(S[stree.query(fu, fv+1)[1]])

        ll, mm, ms = iin[x], mmn[x], msn[x]
        uvcs = []
        for target_i in [F[u], F[v], F[cc]]:
            index = bsearch(ll, target_i, 0, len(ll)-1)
            uvcs.append((mm[index], ms[index]))
        diff = (uvcs[0][0] + uvcs[1][0] - 2 * uvcs[2][0]) * y - (uvcs[0][1] + uvcs[1][1] - 2 * uvcs[2][1])
        print(depthh[u] + depthh[v] - 2*depthh[cc] + diff)


if __name__ == '__main__':
    process()
