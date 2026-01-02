class Unionfind:

    __slots__ = ['nodes']

    def __init__(self, n):
        self.nodes = [-1]*n

    def root(self, x):
        if self.nodes[x] < 0:
            return x
        else:
            root_x = self.root(self.nodes[x])
            self.nodes[x] = root_x
            return root_x

    def unite(self, x, y):
        x = self.root(x); y = self.root(y)
        if x == y:
            return
        rank_x = -self.nodes[x]; rank_y = -self.nodes[y]
        if rank_x < rank_y:
            x, y = y, x
        if rank_x == rank_y:
            self.nodes[x] -= 1
        self.nodes[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def rank(self, x):
        return -self.nodes[self.root(x)]

N,M = map(int,input().split())
info = [list(map(int,input().split())) for i in range(M)]

def bridge(k):
    uf = Unionfind(N)
    for i,pair in enumerate(info):
        if i == k: continue
        a = pair[0] - 1; b = pair[1] - 1
        uf.unite(a,b)
    s = {uf.root(i) for i in range(N)}
    if len(s) != 1:
        return True
    return False

cnt = 0
for k in range(M):
    if bridge(k):
        cnt += 1

print(cnt)