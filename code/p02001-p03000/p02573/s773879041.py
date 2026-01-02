def main():
    class unionfind():
        # size:要素数,tree：unionfind木
        def __init__(self, size):  # self,要素数
            self.size = size
            self.tree_root = list(range(self.size))
            self.tree_depth = [1]*self.size

        # rootを探す
        def root(self, index):
            temp_list = []
            temp = self.tree_root[index]
            while index != temp:
                temp_list.append(index)
                index = temp
                temp = self.tree_root[index]
            for i in temp_list:
                self.tree_root[i] = index
            return index

        # 結合
        def unite(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            if r1 != r2:
                d1, d2 = self.tree_depth[r1], self.tree_depth[r2]
                if d1 <= d2:
                    self.tree_root[r1] = r2
                    self.tree_depth[r2] = max(d1+1, d2)
                else:
                    self.tree_root[r2] = r1
                    self.tree_depth[r1] = max(d2+1, d1)

        # 同じか判定
        def same(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            return r1 == r2

        # 連結成分の個数
        def component(self):
            return len({self.root(i) for i in range(self.size)})

    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in [0]*m]
    s = [0]*n
    uf = unionfind(n)

    for a, b in ab:
        uf.unite(a-1, b-1)

    for i in range(n):
        s[uf.root(i)] += 1
    print(max(s))


main()
