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



def main():
    N = int(input())
    nodes = []
    for i in range(N):
        x, y = map(int, input().split())
        nodes.append((x, y, i))

    uf = UnionFind(N)
    nodes_sorted_by_x = sorted(nodes)
    nodes_sorted_by_y = sorted(nodes, key=lambda i: i[1])

    edges = []
    for i in range(N - 1):
        dx = abs(nodes_sorted_by_x[i][0] - nodes_sorted_by_x[i + 1][0])
        dy = abs(nodes_sorted_by_x[i][1] - nodes_sorted_by_x[i + 1][1])
        cost = min(dx, dy)
        edges.append((cost, nodes_sorted_by_x[i][2],  nodes_sorted_by_x[i + 1][2]))

    for i in range(N - 1):
        dx = abs(nodes_sorted_by_y[i][0] - nodes_sorted_by_y[i + 1][0])
        dy = abs(nodes_sorted_by_y[i][1] - nodes_sorted_by_y[i + 1][1])
        cost = min(dx, dy)
        edges.append((cost, nodes_sorted_by_y[i][2],  nodes_sorted_by_y[i + 1][2]))

    edges.sort()
        
    ans = 0
    for edge in edges:
        w, s, t = edge
        if not uf.same(s, t):
            ans += w
            uf.union(s, t)
    print(ans)

    #print(nodes_sorted_by_x)
    #print(nodes_sorted_by_y)
if __name__ == '__main__':
    main()
