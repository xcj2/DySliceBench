def main():
    class UnionFind:
        def __init__(self, N):
            """
            N:要素数
            root:各要素の親要素の番号を格納するリスト.
                ただし, root[x] < 0 ならその頂点が根で-root[x]が木の要素数.
            rank:ランク
            """
            self.N = N
            self.root = [-1] * N
            self.rank = [0] * N

        def find(self, x):
            """頂点xの根を見つける"""
            if self.root[x] < 0:
                return x
            else:
                while self.root[x] >= 0:
                    x = self.root[x]
                return x

        def union(self, x, y):
            """x,yが属する木をunion"""
            # 根を比較する
            # すでに同じ木に属していた場合は何もしない.
            # 違う木に属していた場合はrankを見てくっつける方を決める.
            # rankが同じ時はrankを1増やす
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return
            elif self.rank[x] > self.rank[y]:
                self.root[x] += self.root[y]
                self.root[y] = x
            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

        def same(self, x, y):
            """xとyが同じグループに属するかどうか"""
            return self.find(x) == self.find(y)

    import sys
    n, q = map(int, sys.stdin.buffer.readline().split())
    uf = UnionFind(n)
    for i in range(q):
        t, u, v = map(int, input().split())
        if t:
            print(int(uf.same(u, v)))
        else:
            uf.union(u, v)


main()
