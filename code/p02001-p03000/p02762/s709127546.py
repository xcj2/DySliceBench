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
        

from collections import defaultdict, Counter
count_friend = Counter()
# friends = defaultdict(list)
friends_cluster = Counter()
# blocks = defaultdict(set)
count_block = Counter()
N, M, K = map(int, input().split())
ds = DisjointSet(N+1)
# graph = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    ds.unite(A, B)
    count_friend[A] += 1
    count_friend[B] += 1
for i in range(K):
    C, D = map(int, input().split())
    if ds.same(C, D):
        count_block[C] += 1
        count_block[D] += 1
c_ids = [ds.findSet(i) for i in range(N+1)]
for i in range(1, N+1):
    friends_cluster[c_ids[i]] += 1
ans = []
for i in range(1, N+1):
    c_id = c_ids[i]
    ans += [friends_cluster[c_id]-count_block[i]-count_friend[i]-1]
print(' '.join(list(map(str, ans))))
# print(ds.p)