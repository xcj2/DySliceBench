import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

class SegmentTree():
    f = max
    unit = 0
   
    def __init__(self,array):
        self.N = len(array)
        self.tree = [self.unit] * (2*self.N)
        #self._build(array)
    
    def _build(self,array):
        for i,x in enumerate(array,self.N):
            self.tree[i] = x
        for i in range(self.N - 1,0,-1):
            self.tree[i] = self.f(self.tree[i << 1],self.tree[i << 1|1])
    
    def update(self,k,x):
        k += self.N
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.f(self.tree[k << 1],self.tree[k << 1|1])
    
    def query(self,l,r):
        l += self.N
        r += self.N
        vl = self.unit
        vr = self.unit
        while l < r:
            if l&1: 
                vl = self.f(vl,self.tree[l])
                l += 1
            if r&1:
                r -= 1
                vr = self.f(self.tree[r],vr)
            l >>= 1
            r >>= 1
        return self.f(vl,vr)
    
    def __str__(self):
        return '\n'.join(' '.join(str(v) for v in self.tree[1<<i:1<<(i + 1)]) for i in range((2*self.N).bit_length()))

N = int(input())
A = list(map(int,input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

B = sorted(list(set(A)))
M = len(B)
toID = {i:j for i,j  in zip(B,range(1,M + 1))}
dp = SegmentTree([0] * (M + 1))
ans = [0] * N
before = [0] * N

def dfs(v,p = -1):
    idx = toID[A[v]]
    a = dp.query(0,idx) + 1
    before[v] = dp.query(idx,idx + 1)
    flag = False
    if before[v] < a:
        flag = True
        dp.update(idx,a)
    before_max = dp.query(0,M + 1)
    ans[v] = max(before_max,a)
    for e in G[v]:
        if e == p:
            continue
        dfs(e,v)
    if flag:
        dp.update(idx,before[v])

dfs(0)
print('\n'.join(map(str,ans)))