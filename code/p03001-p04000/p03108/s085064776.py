#!/usr/bin/env python3
import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x): # 根を探す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N,M=MAP()
    
    edges = []
    for _ in range(M):
        a,b = MAP()
        edges.append((a-1,b-1))

    # グループ数C2が
    answer = [0]*M
    answer[M-1] = N*(N-1)//2
    uf = UnionFind(N)

    for i in range(M-1,0,-1):
        a,b = edges[i]
        if uf.same(a,b):
            answer[i-1] = answer[i]
            continue

        answer[i-1] = answer[i]-uf.size(a)*uf.size(b)
        uf.union(a,b)
    
    for i in range(M):
        print(answer[i])
    return

if __name__ == '__main__':
    main()
