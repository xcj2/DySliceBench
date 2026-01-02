# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127
from math import sqrt
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

class UnionFind:
    def __init__(self, n):
        # 初期状態は全要素が根なので、親は自分自身
        self.par = [i for i in range(n+1)]
        # 集団の要素数(size)を格納する(初期は全て1)
        self.size = [1] * (n+1)
    
    # 根を検索する関数
    def find(self, x):
        # 根までたどったらその番号を返す
        if self.par[x] == x:
            return x
        # 根でないなら親の要素で再検索
        else:
            # 検索過程で親を書き換える(圧縮経路)
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])
  
    # 結合(unite)する関数
    def unite(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        # サイズを比較し、小さい方を大きい方に繋げる
        if self.size[x] < self.size[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
           
    # 同じグループに属するかを判定する関数
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要素が属する木のサイズを返す関数
    def get_size(self, x):
        return self.size[self.find(x)]
    
    # グループ数を返す関数
    def group_sum(self):
        c = 0
        for i in range(len(self.par)):
            if self.find(i) == i:
                c += 1
        return c
    

def Kruskal(V, Edges):
    """
    E: E[i] = (from, to, weight)として辺を格納したリスト
    """
    # 重みでソートする
    Edges.sort(key=lambda x: x[2])

    uf = UnionFind(V)
    weight = 0
    for s, t, w in Edges:
    	# s, tが連結なら閉路を作ってしまう。
    	if uf.is_same(s, t):
        	    continue
    	# s, tを繋げても閉路にならないとき
    	else:
        	weight += w
        	uf.unite(s, t)

    return weight


def main():
    ans = []
    #with open("AOJ\\in.txt", "r") as f:

    while True:
        n = int(readline())
        if n == 0:
            break
            
        xyzr = [tuple(map(float, readline().split()))for _ in range(n)]
        E = []
        for i in range(n-1):
            x_i, y_i, z_i, r_i = xyzr[i]
            for j in range(i+1,n):
                x_j, y_j, z_j, r_j = xyzr[j]
                d = sqrt((x_i - x_j)**2 + (y_i - y_j)**2 + (z_i - z_j)**2)
                length = max(d - (r_i + r_j), 0.0)
                E.append((i, j, length))

        # クラスカル法
        weight = Kruskal(n, E)
        ans.append(weight)

    print("\n".join("{:.3f}".format(i) for i in ans))


if __name__ == "__main__":
    main()
