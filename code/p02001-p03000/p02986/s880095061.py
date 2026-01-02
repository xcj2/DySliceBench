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
    for u in G[1][::-1]:
        stack += [-1, u]

    visited = set([1])
    depth, depthh = [0]*(N+1), [0]*(N+1)
    mmn = [[0] for _ in range(N)]
    msn = [[0] for _ in range(N)]
    iin = [[] for _ in range(N)]
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

            for u in G[v][::-1]:
                if u in visited:
                    continue
                stack += [-v, u]
        else:
            child = path.pop()
            cc, dpd = dp[(min(-v, child), max(-v, child))]
            mmn[cc].append(mmn[cc][-1]-1)
            iin[cc].append(ii)
            msn[cc].append(msn[cc][-1]-dpd)
            S[ii] = v
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

        if len(mmn[x])-1 == 0:
            diff = 0
        else:
            ll, mm, ms, lncc = iin[x], mmn[x], msn[x], len(mmn[x])-2
            uvcs = []
            for target_i in [F[u], F[v], F[cc]]:
                ind, lw, hw =  (len(mmn[x])-2)//2, 0, len(mmn[x]) - 2
                if target_i < ll[0] or target_i >= ll[lncc]:
                    uvcs.append((0,0))
                else:
                    while True:
                        if ll[ind] <= target_i:
                            if target_i < ll[ind+1]:
                                uvcs.append((mm[ind+1], ms[ind+1]))
                                break
                            ind, lw = (ind+1 + hw)//2, ind+1
                            continue
                        ind, hw = (ind-1 + lw)//2, ind-1
            diff = (uvcs[0][0] + uvcs[1][0] - 2 * uvcs[2][0]) * y - (uvcs[0][1] + uvcs[1][1] - 2 * uvcs[2][1])
        print(depthh[u] + depthh[v] - 2*depthh[cc] + diff)


if __name__ == '__main__':
    process()
