# ABC133 オイラーツアー
import sys
from collections import defaultdict
readline = sys.stdin.readline
N, Q = map(int, readline().split())

vs = set()
def dfs_w(v, d):

    S, F, depth, depthh = [], [None]+[0]*N, [-1] + [0]*N, [0] + [0]*N
    mmn, msn, iin = [[0] for _ in range(N)], [[0] for _ in range(N)], [[0] for _ in range(N)]

    pvs, stack, path = set(), [(1, 0, 0)], [0]
    # dfs while版 
    while True:
        if len(stack) == 0:
            break
        v, cc, dpd = stack.pop()
        if v > 0:
            parent = path[-1]
            path.append(v)
            pvs.add(v)
            vs.add(v)

            F[v] = len(S)
            depth[v], depthh[v] = depth[parent] + 1, depthh[parent] + dpd
            mmn[cc].append(mmn[cc][-1]+1)
            msn[cc].append(msn[cc][-1]+dpd)
            iin[cc].append(len(S))

            S.append(v)
            for u, ucc, udpd in d[v]:
                if u in pvs:
                    continue
                    # 閉路あり
                    for i, c in enumerate(path):
                        if c == u:
                            break
                    return path[i+1:]  + [u]
                if u in vs:
                    continue
                stack += [(-v, ucc, udpd), (u, ucc, udpd)]
        else:
            pvs.remove(path[-1])
            path.pop()
            mmn[cc].append(mmn[cc][-1]-1)
            msn[cc].append(msn[cc][-1]-dpd)
            iin[cc].append(len(S))
            S.append(v)

    return S, F, depth, depthh, mmn, msn, iin

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
    G = [set() for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c, d = map(int, readline().split())
        G[a].add((b,c,d))
        G[b].add((a,c,d))

    S, F, depth, depthh, mmn, msn, iin = dfs_w(1, G)

    stree = SegTree([(depth[abs(v)], i) for i, v in enumerate(S)], len(S), (N, None), min)
    for _ in range(Q):
        x, y, u, v = map(int, readline().split())
        fu, fv = sorted([F[u], F[v]])
        cc = abs(S[stree.query(fu, fv+1)[1]])

        r = depthh[u] + depthh[v] - 2*depthh[cc]
        index = bsearch(iin[x], F[u], 0, len(iin[x])-1)
        r += mmn[x][index] * y - msn[x][index]
        index = bsearch(iin[x], F[v], 0, len(iin[x])-1)
        r += mmn[x][index] * y - msn[x][index]

        index = bsearch(iin[x], F[cc], 0, len(iin[x])-1)
        r -= 2 * (mmn[x][index] * y - msn[x][index])
        print(r)

if __name__ == '__main__':
    process()
