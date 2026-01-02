class UnionFind(object):
 
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]
 
    def find(self, x):
        if self.table[x] < 0:
            return x
        self.table[x] = self.find(self.table[x])
        return self.table[x]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 == s2:
            return False
        if self.table[s1] > self.table[s2]:
            s1, s2 = s2, s1
        self.table[s1] += self.table[s2]
        self.table[s2] = s1
        return True

H, W = list(map(int, input().split()))
S = list(input() for _ in range(H))
uf = UnionFind(H*W)

def get(h, w):
    return h * W + w

for h in range(H):
    for w in range(W):        
        for dh, dw in zip((0, 1), (1, 0)):
            if (h + dh) >= H or (w + dw) >= W:
                continue
            if S[h][w] != S[h+dh][w+dw]:
                uf.union(get(h, w), get(h+dh, w+dw))


from itertools import product

C1 = []
C2 = []

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            C1.append((h, w))
        else:
            C2.append((h, w))

white = [0] * (H * W)
black = [0] * (H * W)

for h in range(H):
    for w in range(W):
        n = get(h, w)
        par = uf.find(n)
        # print(h, w, n, par)
        if par < 0:
            par = n
        if S[h][w] == ".":
            white[par] += 1
        else:
            black[par] += 1
            
ans = 0
# print(white)
# print(black)
for h in range(H):
    for w in range(W):
        n = get(h, w)
        ans += white[n] * black[n]
print(ans)
            

