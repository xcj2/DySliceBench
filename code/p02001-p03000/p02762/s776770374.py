#!/usr/bin/env python3
import sys

class UnionFind():
    def __init__(self, n):
        self.n = n
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

def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    return


def main():
    N, M, K = map(int, input().split())
    connection = [[] for _ in range(N)]
    uf = UnionFind(N)
    for i in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        connection[a].append(b)
        connection[b].append(a)
        uf.union(a, b)

    for i in range(K):
        c, d = map(lambda x: int(x) - 1, input().split())
        if uf.same(c, d):
            connection[c].append(d)
            connection[d].append(c)

    ans = []
    for i in range(N):
        ans.append(uf.size(i) - len(connection[i]) - 1)
    L = [str(i) for i in ans]
    print(" ".join(L))


if __name__ == '__main__':
    main()
