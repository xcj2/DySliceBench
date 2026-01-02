# 66

from decimal import *
import heapq

class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [int(x) for x in range(n)]
        
    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def unite(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x == p_y:
            return False
        if self.rank[p_x] < self.rank[p_y]:
            self.par[p_x] = p_y
            self.rank[p_x] += 1
        else:
            self.par[p_y] = p_x
            self.rank[p_y] += 1
        return True
    
    def same(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x == p_y:
            return True
        else:
            return False
    
while True:
    N = int(input())
    if N == 0:
        exit(0)
    C_L = [[int(Decimal(x) * (10**3)) for x in input().split()] for y in range(N)]
    
    UF = UnionFind(N)
    hq = []
    for i in range(N):
        i_x, i_y, i_z, i_r = C_L[i]
        for j in range(i+1,N):
            j_x, j_y, j_z, j_r = C_L[j]
            _d = ((i_x - j_x)**2 + (i_y - j_y)**2 + (i_z - j_z)**2) ** (0.5) - i_r - j_r
            hq.append([_d, i, j])
#     print(hq)
#     print("HOGE")
    ans = 0
    heapq.heapify(hq)
    while len(hq) > 0:
        _d, _i, _j = heapq.heappop(hq)
        if UF.same(_i, _j):
            continue
        ans += max(_d, 0)
        UF.unite(_i, _j)
    print("{:.3f}".format(ans / (10**3)))


