from collections import defaultdict

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.rank = [1]*(N)

    def getroot(self, x):
        if self.parent[x] == x:
            return x
        else:
            root = self.getroot(self.parent[x])
            self.parent[x] = root
            return root

    def is_group(self, x,y):
        return self.getroot(x) == self.getroot(y)

    def union(self, x, y):
        rootx = self.getroot(x)
        rankx = self.rank[rootx]
        rooty = self.getroot(y)
        ranky = self.rank[rooty]
        if rankx > ranky:
            self.parent[rooty] = rootx
        else:
            self.parent[rootx] = rooty
            self.rank[rooty] = max(self.rank[rooty], self.rank[rootx]+1)

n, k, l = map(int, input().split())

loads = UnionFind(n)
rails = UnionFind(n)

for _ in range(k):
    x, y = map(int, input().split())
    loads.union(x-1, y-1)

for _ in range(l):
    x, y = map(int, input().split())
    rails.union(x-1, y-1)

pair = defaultdict(int)
for i in range(n):
    pair[(loads.getroot(i), rails.getroot(i))] += 1

ans = "" 
for i in range(n-1):
    ans += str(pair[(loads.getroot(i), rails.getroot(i))]) + " "
ans += str(pair[(loads.getroot(n-1), rails.getroot(n-1))])
print(ans)
