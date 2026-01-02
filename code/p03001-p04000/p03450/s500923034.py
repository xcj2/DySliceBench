"""
https://atcoder.jp/contests/abc087/tasks/arc090_b

xR-xL = D
Mこの情報が正しいかどうかの判定
グループを作って、グループ内の拘束条件があっているか確認
重み付きunionfindを使う
https://qiita.com/drken/items/cce6fc5c579051e64fab
http://at274.hatenablog.com/entry/2018/02/03/140504


5 5
1 2 2
2 3 3
4 5 4
2 5 10
3 4 3
"""

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

    ### 重みが正負逆になる。なんでだ
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


N,M = map(int, input().split())
uf = UnionFind(N)
for i in range(N):
    uf.find(i)

for i in range(M):
    l,r,d = map(int, input().split())
    # 初めて出てくる奴らは数直線形成に使う
    if not uf.judge(l, r):
        uf.weighted_union(l, r, d)
    # 二回目のやつらは後で拘束条件に使う
    else:
        if d == uf.weight[r] - uf.weight[l]:
            continue
        else:
            print("No")
            exit()
print("Yes")
# for i in uf.parent.keys():
#     uf.find(i)
#     print("index:{} rank:{}, parent:{}, weight:{}".format(i,uf.rank[i],uf.parent[i],uf.weight[i]))
