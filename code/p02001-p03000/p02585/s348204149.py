from collections import defaultdict
inpl = lambda: list(map(int,input().split()))
class UnionFind:
    def __init__(self, N=None):
        if N is None or N < 1:
            self.parent = defaultdict(lambda: -1)
        else:
            self.parent = [-1]*int(N)

    def root_rec(self, n):
        if self.parent[n] < 0:
            return n
        else:
            m = self.root(self.parent[n])
            self.parent[n] = m
            return m

    def root(self, n):
        stack = []
        while n >= 0:
            stack.append(n)
            n = self.parent[n]
        m = stack.pop()
        while stack:
            self.parent[stack.pop()] = m
        return m

    def merge(self, m, n):
        rm = self.root(m)
        rn = self.root(n)
        if rm != rn:
            if -self.parent[rm] < -self.parent[rn]:
                rm, rn = rn, rm
            self.parent[rm] += self.parent[rn]
            self.parent[rn] = rm

    def size(self, n):
        return -self.parent[self.root(n)]
    
    def connected(self, m, n):
        return self.root(m) == self.root(n)

    def groups(self):
        if isinstance(self.parent,list):
            return list(filter(lambda i: self.parent[i]<0, range(len(self.parent))))
        else: # self.parent: defaultdict
            return list(filter(lambda i: self.parent[i]<0, self.parent.keys()))
 
    def groups_num(self):
        return len(self.groups())

    def elements(self):
        if isinstance(self.parent,list):
            return range(len(self.parent))
        else:
            return self.parent.keys()

N, K = inpl()
P = list(map(lambda x: x-1,inpl()))
C = inpl()

uf = UnionFind(N)
for i in range(N):
    uf.merge(i, P[i])

ans = C[0]
for g in uf.groups():
    L = uf.size(g)
    cycle = C[g]
    p = P[g]
    while p != g:
        cycle += C[p]
        p = P[p]
    q, r = K//L, K % L
    if cycle > 0:
        score = q * cycle
    else:
        score = 0

    s = g
    for _ in range(L):
        u = score
        t = s
        for i in range(L):
            u += C[t]
            t = P[t]
            if i == r:
                if q > 0 and cycle > 0:
                    u -= cycle
                elif q > 0 and cycle <= 0:
                    pass
                elif q == 0:
                    break
            if u > ans:
                ans = u
        s = P[s]

print(ans)
