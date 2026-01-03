#!/usr/bin/env python3
import sys
import heapq
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

def solve(N: int, x: "List[int]", y: "List[int]"):
    xy = []
    edges = [] # cost,node1,node2
    for i in range(N):
        xy.append((i,x[i],y[i]))

    x_xy = sorted(xy, key= lambda x:x[1])
    y_xy = sorted(xy, key= lambda x:x[2])
    
    for i in range(N-1):
        cur = x_xy[i]
        next = x_xy[i+1]
        edges.append((next[1]-cur[1],next[0],cur[0]))
        cur = y_xy[i]
        next = y_xy[i+1]
        edges.append((next[2]-cur[2],next[0],cur[0]))

    edges.sort(key= lambda x: x[0])
    uf = UnionFind(N)
    answer = 0
    
    for cost,node1,node2 in edges:
        if uf.same(node1,node2):
            continue

        answer += cost
        uf.union(node1,node2)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()
