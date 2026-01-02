import sys
from operator import add
readline = sys.stdin.readline

def euler_tour(root, Edge):
    N = len(Edge)
    stack = [root]
    used = [False]*N
    tour = []
    down = []
    dist = [0]*N
    ta = tour.append
    sa = stack.append
    St = [None]*N
    En = [None]*N
    cnt = -1
    while stack:
        cnt += 1
        vn = stack.pop()
        ta(vn)
        
        if St[vn] is None:
            St[vn] = cnt
        En[vn] = cnt
        if used[vn]:
            continue
        for vf in Edge[vn]:
            if used[vf]:
                sa(vf)
            else:
                dist[vf] = 1+dist[vn]
                down.append(vf)
        stack.extend(down)
        down = []
        used[vn] = True
    return St, En, tour, dist

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p):
        if v == -1:
            continue
        res[v].append(i)
    return res

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
            
    def __repr__(self):
        return str(' '.join(map(str, self.data[self.N0:self.N0+self.N])))

    
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
    
    def binsearch(self, l, r, check, reverse = False):
        L, R = l+self.N0, r+self.N0
        SL, SR = [], []
        while L < R:
            if R & 1:
                R -= 1
                SR.append(R)
            if L & 1:
                SL.append(L)
                L += 1
            L >>= 1
            R >>= 1
        
        if reverse:
            for idx in (SR + SL[::-1]):
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.data[2*idx+1]):
                    idx = 2*idx + 1
                else:
                    idx = 2*idx
            return idx - self.N0
        else:
            for idx in (SL + SR[::-1]):
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.data[2*idx]):
                    idx = 2*idx
                else:
                    idx = 2*idx + 1
            return idx - self.N0

N = int(readline())
Col = list(map(lambda x: int(x)-1, readline().split()))
Colidx = [[] for _ in range(N)]
for i in range(N):
    Colidx[Col[i]].append(i)

Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)


root = 0
for root in range(N):
    if len(Edge[root]) == 1:
        break
P, L = parorder(Edge, root)
C = getcld(P)

St, En, tour, dist = euler_tour(root, Edge)

L = len(tour)
table = [0]*L
Ans = [0]*N
for i in range(N):
    table[En[i]] = 1

T = Segtree(table, 0, initialize = True, segf = add)
for c in range(N):
    Ci = Colidx[c]
    if Ci:
        Ci.sort(key = lambda x: dist[x], reverse = True)
        res = 0
        for v in Ci:
            sv = 0
            for cv in C[v]:
                k = T.query(St[cv], En[cv]+1)
                sv += k
                res += k*(k+1)//2
            T.update(En[v], -sv)
        k = T.query(St[root], En[root]+1)
        
        res += k*(k+1)//2
        for v in Ci:
            T.update(En[v], 1)
        Ans[c] = N*(N+1)//2-res
print('\n'.join(map(str, Ans)))
