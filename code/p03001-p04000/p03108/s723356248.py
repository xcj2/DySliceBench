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
    

def main():
    N,M,*ab = map(int, read().split())
    
    E = [(a, b) for a, b in zip(*[iter(ab)]*2)]

    pair = N * (N - 1) // 2
    ans = []

    uf = UnionFind(N)
    con = 0
    for a, b in reversed(E):
        ans.append(pair)
        if not uf.is_same(a, b):
            n_a = uf.get_size(a)
            n_b = uf.get_size(b)
            pair -= n_a * n_b

        uf.unite(a, b)

    print("\n".join(map(str, ans[::-1])))


if __name__ == "__main__":
    main()
