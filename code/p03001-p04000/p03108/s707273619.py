#!/usr/bin/env python3
import sys

class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
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
        

def main():
    N, M = map(int, input().split())
    A = [None] * M
    B = [None] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = [0] * M
    ans[-1] = N * (N-1) // 2
    # 逆順に橋が出来ると不便さが変わるか調べる
    uf = UnionFind(N)
    for i in range(M-1):
        # aとbが連結か調べる
        a, b = A[M-1-i]-1, B[M-1-i]-1
        if uf.find(a) == uf.find(b):
            ans[M-i-2] = ans[M-i-1]
        else:
            ans[M-i-2] = ans[M-i-1] - abs(uf.parents[uf.find(a)]) * abs(uf.parents[uf.find(b)])
            uf.union(a, b) 

    [print(a) for a in ans]
    

if __name__ == '__main__':
    main()
