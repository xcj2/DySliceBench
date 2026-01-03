from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
    
    def __init__(self, n):
        self.parents = [-1]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):

        x = self.find(x)
        y = self.find(y)  

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x,y = y,x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

N,K,L = map(int, input().split())

road_union = UnionFind(N)
rails_union = UnionFind(N)

for i in range(K):
    p,q = map(int, input().split())
    p -= 1
    q -= 1

    road_union.union(p,q)
for i in range(L):
    r,s = map(int, input().split())

    r -= 1
    s -= 1
    rails_union.union(r,s)

d = defaultdict(int)

for i in range(N):
    d[(road_union.find(i), rails_union.find(i))] += 1


print(*[d[(road_union.find(i),rails_union.find(i))] for i in range(N)])