class UnionFindTree():
    def __init__(self, values=[]):
        self.parent_of = {}
        self.rank_of = {}
        for value in values:
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
    N, M = map(int, input().split())
    P = [x-1 for x in map(int, input().split())]
    uft = UnionFindTree(P)
    for _ in range(M):
        p, q = [x-1 for x in map(int, input().split())]
        uft.unite(P[p], P[q])
    ans = 0
    for i in range(N):
        if uft.is_same(i, P[i]):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
