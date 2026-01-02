class UnionFindTree():
    def __init__(self, values=[]):
        self.parent_of = {}
        self.rank_of = {}
        for value in values:
            self.add(value)

    def add(self, value):
        if value in self.parent_of:
            raise RuntimeError("Dupulicated Value Added")
        self.parent_of[value] = None
        self.rank_of[value] = 0

    def __root(self, value):
        if self.parent_of[value] is None:
            return value
        else:
            self.parent_of[value] = self.__root(self.parent_of[value])
            return self.parent_of[value]

    def unite(self, a, b):
        r1 = self.__root(a)
        r2 = self.__root(b)
        if r1 != r2:
            if self.rank_of[r1] < self.rank_of[r2]:
                self.parent_of[r1] = r2
            else:
                self.parent_of[r2] = r1
                if self.rank_of[r1] == self.rank_of[r2]:
                    self.rank_of[r1] += 1

    def is_same(self, a, b):
        return self.__root(a) == self.__root(b)

    def groups(self):
        groups = {}
        for k in self.parent_of.keys():
            r = self.__root(k)
            if r not in groups:
                groups[r] = []
            groups[r].append(k)
        return [groups[x] for x in groups]


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    uft = UnionFindTree()
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                uft.add((i, j))
                if i >= 1 and S[i-1][j] == '#':
                    uft.unite((i, j), (i-1, j))
                if j >= 1 and S[i][j-1] == '#':
                    uft.unite((i, j), (i, j-1))
    for g in uft.groups():
        if len(g) == 1:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
