from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        class KeyDict(dict):
            # 辞書にないときの対応
            def __missing__(self,key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = defaultdict(int)
        self.weight = defaultdict(int)

    # 根を探す
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # 経路圧縮
            # 自分自身じゃない場合は、上にさかのぼって検索(再帰的に)
            y = self.find(self.parent[x])           
            self.weight[x] += self.weight[self.parent[x]]   #圧縮時にweightを更新(和)
            self.parent[x] = y      #親の置き換え(圧縮)
            return self.parent[x]

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    ### 重み付き
    def weighted_union(self, x, y, w):
        # print("unite",x,y,w,self.weight)
        px = self.find(x)
        py = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        # if px == py: return 0
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.weight[px] = - w - self.weight[x] + self.weight[y]
        else:
            self.parent[py] = px
            self.weight[py] =  w + self.weight[x] - self.weight[y]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return 0

    # 判定
    def judge(self, x, y):
        return self.find(x) == self.find(y)


H,W = map(int, input().split())
fields = [list(input()) for i in range(H)]
uf = UnionFind(H*W)
for i in range(H):
    for j in range(W):
        if i-1 >= 0 and fields[i][j] != fields[i-1][j]:
            uf.union(i*W+j,(i-1)*W+j)
        if j-1 >= 0 and fields[i][j] != fields[i][j-1]:
            uf.union(i*W+j,i*W+j-1)
        if i+1 < H and fields[i][j] != fields[i+1][j]:
            uf.union(i*W+j,(i+1)*W+j)
        if j+1 < W and fields[i][j] != fields[i][j+1]:
            uf.union(i*W+j,i*W+j+1)


cnt_w = defaultdict(int)
cnt_b = defaultdict(int)
ps = set()
for i in range(H):
    for j in range(W):
        p = uf.find(i*W+j)
        ps.add(p)
        if fields[i][j] == ".":
            cnt_w[p] += 1
        else:
            cnt_b[p] += 1
ans = 0
for p in ps:
    ans += cnt_w[p] * cnt_b[p]
print(ans)