import numpy as np

class unionfind: #ノード数nを読み込む
    def __init__(self,n): #コンストラクタ
        self.parent = list(range(n))
    def find(self,a): #根を探す、そのつど根を更新
        if self.parent[a] == a: return a #自分が根だったら終了
        else:
            self.parent[a] = self.find(self.parent[a]) #経路圧縮
            return self.parent[a]
    def unite(self,a,b): #ランク度外視で根を合体する
        pa,pb = self.find(a),self.find(b)
        if pa == pb: return 0 #根が一緒なら何もせず終了
        else: self.parent[pa] = pb
    def same(self,a,b):
        pa,pb = self.find(a),self.find(b)
        return pa == pb

# クラスを使わない実装
def find(x):
    if node[x] == x: return x
    else: node[x] = find(node[x]) ; return node[x]
def unite(x,y):
    x,y = find(x),find(y)
    if x == y : return
    else: node[x] = y
def same(x,y): return find(x) == find(y)


n,m = map(int,input().split())
ab = np.array([list(map(int,input().split())) for i in range(m)])
a,b = ab.T[0] -1, ab.T[1] -1

ans = 0
for i in range(m): #除外する辺を決める
    connect = 0
    node = list(range(n))
    for j in range(m): #i以外の辺についてuniteしていく
        if i != j and  not same(a[j],b[j]): unite(a[j],b[j]) ; connect += 1
    ans += 0 if connect == n-1 else 1
print(ans)

