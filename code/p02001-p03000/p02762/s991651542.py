class UnionFind:
    def __init__(self, n):
        self.par = [-1 for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if not x==y: # 根が同じでない場合のみ併合する
            if self.rank[x] < self.rank[y]:
                self.par[y] += self.par[x] # 要素数を併合
                self.par[x] = y # 根を付け替えている
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
        
    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y) 

import sys
input = sys.stdin.readline
from collections import defaultdict

N,M,K = map(int,input().split())
Fr = [0]*N
FrKi = UnionFind(N)
Bl = defaultdict(list)

for i in range(M):
    A,B = map(int,input().split())
    A -=1
    B-=1
    Fr[A]+=1
    Fr[B]+=1
    FrKi.union(A,B)
    
for i in range(K):
    A,B = map(int,input().split())
    A-=1
    B-=1
    Bl[A].append(B)
    Bl[B].append(A)
    
Ans = [0]*N
#print(FrKi.par)
#print(Fr)
for i in range(N):
    tmp = -FrKi.par[FrKi.find(i)] - Fr[i] -1
    for j in Bl[i]:
        if FrKi.same_check(i,j):
            tmp -= 1
    Ans[i] = tmp
print(*Ans)