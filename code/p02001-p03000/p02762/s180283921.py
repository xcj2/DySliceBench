class union():
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.friends = [0 for i in range(n)]
        self.blocks = [[] for i in range(n)]
        self.counts = [1] * n
        self.block_counts = [0] * n
    def find(self, n):
        if self.par[n] == n:
            return n
        else:
            return self.find(self.par[n])
    def block(self, a, b):
        self.blocks[a].append(b)
        self.blocks[b].append(a)
        if self.same(a, b):
            self.block_counts[a] += 1
            self.block_counts[b] += 1
    def unite(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.friends[a] += 1
        self.friends[b] += 1
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.counts[y] += self.counts[x]
        else:
            self.par[y] = x
            self.counts[x] += self.counts[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same(self, a, b):
        return self.find(a) == self.find(b)
    def optimize(self):
        self.par = list(map(self.find, self.par))
def main():
    N, M, K = map(int, input().split())
    AB = [list(map(lambda x:int(x)-1, input().split())) for i in range(M)]
    CD = [list(map(lambda x:int(x)-1, input().split())) for i in range(K)]
    u = union(N)
    unite = u.unite
    block = u.block
    for a, b in AB:
        unite(a, b)
    for c, d in CD:
        block(c, d)
    counts = u.counts
    par = u.par
    friends = u.friends
    block_counts = u.block_counts
    result = [str(counts[u.find(i)] - friends[i] - block_counts[i] - 1) for i in range(N)]
    print(" ".join(result))
main()