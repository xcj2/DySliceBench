from collections import defaultdict
class DisjointSet:
    def __init__(self, size):
        self.rank = [0 for i in range(size)]
        self.p = [0 for i in range(size)]
        for i in range(size):
            self.makeSet(i)
    
    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    
    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]
        
N, M = map(int, input().split())
P = list(map(int, input().split()))
ds = DisjointSet(N)
p_dict = defaultdict(list)
i_dict = defaultdict(list)

for m in range(M):
    x, y = map(int, input().split())
    ds.unite(x-1, y-1)
# print(ds.p)
for i in range(N):
    dsp = ds.findSet(i)
    p_dict[dsp] += [P[i]]
    i_dict[dsp] += [i+1]
ans = 0
for key in p_dict.keys():
    ans += len(set(p_dict[key]) & set(i_dict[key]))
    # print(key, ans)
print(ans)