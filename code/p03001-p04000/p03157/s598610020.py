def inpl(): return list(map(int, input().split()))

class UnionFind():
    def __init__(self, N):
        self.par = [-1]*(N)
        self.size = [1]*(N)

    def find(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.size[px] += self.size[py]
            self.par[py] = px

H, W = inpl()
S = [[-1]*W for _ in range(H)]
for h in range(H):
    s = input()
    for w in range(W):
        S[h][w] = int(s[w] == "#")

UF = UnionFind(H*W)

for h in range(H):
    for w in range(W-1):
        if S[h][w] != S[h][w+1]:
            UF.unite(h*W+w, h*W+w+1)
for h in range(H-1):
    for w in range(W):
        if S[h][w] != S[h+1][w]:
            UF.unite(h*W+w, h*W+w+W)

ans = 0
for i in range(H*W):
    if UF.par[i] == -1:
        s = UF.size[i]
        ans += s*(s-1)//2

BC = [0]*(H*W)
WC = [0]*(H*W)

for h in range(H):
    for w in range(W):
        if S[h][w] == 1:
            BC[UF.find(h*W+w)] += 1
        else:
            WC[UF.find(h*W+w)] += 1
print(sum([BC[i]*WC[i] for i in range(H*W)]))