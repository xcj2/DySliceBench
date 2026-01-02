
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



n, m = map(int, input().split())
ps = list(map(int, input().split()))

"""    
Unionfindで、自由に移動できるindexを同定
その中で、indexと数字がおなじになるものを同定
"""
uf = UnionFind(n)
for i in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    if not uf.judge(x,y):
        uf.union(x,y)

ps = [p-1 for p in ps]

ans = 0
for i,p in enumerate(ps):
    if uf.judge(i,p):
        ans += 1
        
print(ans)
