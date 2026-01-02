from collections import defaultdict
def inpl(): return list(map(int, input().split()))
H, W = inpl()
G = []

class UnionFindTree():
    
    def __init__(self, N):
        self.parent = [-1]*(N+1)
        self.rank = [1]*(N+1)
        self.size = [1]*(N+1)
  
    def find(self, i):
        if self.parent[i] == -1:
            group = i
        else:
            group = self.find(self.parent[i]) 
            self.parent[i] = group
        return group
      
    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] == self.rank[py]: # rank is same
                self.rank[px] += 1
            elif self.rank[px] < self.rank[py]:
                px, py = py, px
                
            self.parent[py] = px
            self.size[px] += self.size[py]
    
    def getsize(self, x):
        return self.size[self.find(x)]


def binarize(h, w):
    return h*W + w

def reverse(g):
    h, w = divmod(g, W)
    return h, w

UFT = UnionFindTree(H*W)

for _ in range(H):
    G.append(input())

for h in range(H-1):
    for w in range(W):
        if G[h][w] != G[h+1][w]:
            UFT.unite(binarize(h, w),
                      binarize(h+1, w))

for h in range(H):
    for w in range(W-1):
        if G[h][w] != G[h][w+1]:
            UFT.unite(binarize(h, w),
                      binarize(h, w+1))

D = defaultdict(lambda: [0, 0])
for i in range(H*W):
    h, w = reverse(i)
    D[UFT.find(i)][G[h][w] == "."] += 1

ans = 0
for k, v in D.items():
    ans += v[0] * v[1]

print(ans)