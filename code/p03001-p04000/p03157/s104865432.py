H,W = map(int,input().split())
class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False


S = [input() for i in range(H)]
u = UnionFind(H*W)
d = [(-1,0),(1,0),(0,-1),(0,1)]
for x in range(H):
    for y in range(W):
        for dx,dy in d:
            if x+dx<0 or x+dx>=H or y+dy<0 or y+dy>=W:
                continue
            if S[x+dx][y+dy] == S[x][y]:
                continue
            u.union(x+H*y,x+dx+H*(y+dy))

from collections import defaultdict
d = defaultdict(lambda:[[],[]])

for x in range(H):
    for y in range(W):
        if S[x][y] == '#':
            d[u.find(x+H*y)][0].append((x,y))
        else:
            d[u.find(x+H*y)][1].append((x,y))

ans = 0
for key in d:
    ans += len(d[key][0])*len(d[key][1])
print(ans)