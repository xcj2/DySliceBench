

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            # already same
            return

        if self.size[xroot] < self.size[yroot]:
            # merge to yroot
            self.par[xroot] = yroot
            self.size[yroot] = self.size[xroot] + self.size[yroot]
        else:
            # merge to xroot
            self.par[yroot] = xroot
            self.size[xroot] = self.size[xroot] + self.size[yroot]

    def same(self, x, y):
        return self.find(x) == self.find(y)


def read_input():
    n, m, k = map(int, input().split())

    friend_edge = []
    for _ in range(m):
        friend_edge.append(tuple(map(int, input().split())))

    block_edge = []
    for _ in range(k):
        block_edge.append(tuple(map(int, input().split())))

    return n, friend_edge, block_edge


def submit():
    n, friend_edge, block_edge = read_input()

    # 友達関係をUF
    uf = UnionFind(n)
    for a, b in friend_edge:
        uf.unite(a - 1, b - 1)

    # blockか、friend関係にある要素を整理
    # blockかつ、おなじufに含まれるもののみをのこす　
    remove_dict = {i : 0 for i in range(n)}
    for c, d in block_edge:
        if uf.same(c - 1, d - 1):
            remove_dict[c - 1] += 1
            remove_dict[d - 1] += 1
        
    # friend関係を整理
    for a, b in friend_edge:
        remove_dict[a - 1] += 1
        remove_dict[b - 1] += 1

    # result
    result = []
    for i in range(n):
        target_size = uf.size[uf.find(i)]
        result.append(target_size - remove_dict[i] - 1)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    submit()