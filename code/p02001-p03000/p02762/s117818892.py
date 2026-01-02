import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(500000)

# class UnionFind:

#     def __init__(self, n):
#         self.n = n
#         self.parent = [0] * (n+3)
#         self.num = [1] * (n+3)
#         self.diff_weight = [0] * (n+3)
#         for i in range(n):
#             self.parent[i] = i
    
#     def root(self, x):
#         if x == self.parent[x]:
#             return x
#         else:
#             r = self.root(self.parent[x])
#             self.diff_weight[r] += self.diff_weight[self.parent[x]]
#             self.parent[x] = r
#             return r
    
#     def unite(self, a, b, w = 0):
#         w += self.weight(a) - self.weight(b)
#         a = self.root(a)
#         b = self.root(b)
#         if a == b:
#             return
#         self.parent[b] = a
#         sum_v = self.num[a] + self.num[b]
#         self.num[a] = sum_v
#         self.num[b] = sum_v
#         self.diff_weight[b] = w
        
#     def same(self, a, b):
#         return (self.root(a) == self.root(b))
    
#     def sz(self, x):
#         return self.num[self.root(x)]
    
#     def weight(self, x):
#         self.root(x)
#         return self.diff_weight[x]

#     def diff(self, a, b):
#         return self.weight(b) - self.weight(a)

class UnionFind:
    def __init__(self,N):
        self.root = list(range(N+1))
        self.size = [1] * (N+1)
        
    def find_root(self,x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x
    
    def merge(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        sx,sy = self.size[x],self.size[y]
        if sx < sy:
            self.root[x] = y
            self.size[y] += sx
        else:
            self.root[y] = x
            self.size[x] += sy

    def sz(self, x):
        return self.size[x]


if __name__ == "__main__":

    N,M,K = map(int, readline().split())
    A = [0] * (M+5)
    B = [0] * (M+5)
    C = [0] * (K+5)
    D = [0] * (K+5)
    for i in range(M):
        a,b = map(int, readline().split())
        a -= 1
        b -= 1
        A[i] = a 
        B[i] = b 
    for i in range(K):
        a,b = map(int, readline().split())
        a -= 1
        b -= 1
        C[i] = a 
        D[i] = b 
    uf = UnionFind(N)
    for i in range(M):
        uf.merge(A[i], B[i])

    arr = [[] for _ in range(N+2)]
    edge = [[] for _ in range(N+2)]
    for i in range(N):
        arr[uf.find_root(i)].append(i)
    
    for i in range(M):
        if uf.find_root(A[i]) == uf.find_root(B[i]):
            edge[uf.find_root(A[i])].append(i)
    
    for i in range(K):
        if uf.find_root(C[i]) == uf.find_root(D[i]):
            edge[uf.find_root(C[i])].append(i + M)
        

    ans = ["0"] * N
    for i in range(N):
        dd = {}
        if len(arr[i]) == 0:
            continue
        sz = uf.sz(i)
        for j, v in enumerate(arr[i]):
            dd[v] = j
        friends = [0] * (sz+2)
        for e in edge[i]:
            if e <= M-1:
                friends[dd[A[e]]] += 1
                friends[dd[B[e]]] += 1
            else:
                friends[dd[C[e-M]]] += 1
                friends[dd[D[e-M]]] += 1
        for v in arr[i]:
            res = sz - friends[dd[v]] - 1
            ans[v] = str(res)
    print(" ".join(ans))
