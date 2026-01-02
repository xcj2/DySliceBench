class UnionFindTree():
    def __init__(self, values=[]):
        self.__parent_of = {}
        self.__rank_of = {}
        self.__size = {}
        for value in values:
            self.add(value)

    def add(self, value):
        if value in self.__parent_of:
            raise RuntimeError("Dupulicated Value Added")
        self.__parent_of[value] = None
        self.__rank_of[value] = 0
        self.__size[value] = 1

    def __root(self, value):
        if self.__parent_of[value] is None:
            return value
        else:
            self.__parent_of[value] = self.__root(self.__parent_of[value])
            return self.__parent_of[value]

    def unite(self, a, b):
        r1 = self.__root(a)
        r2 = self.__root(b)
        if r1 != r2:
            if self.__rank_of[r1] < self.__rank_of[r2]:
                self.__parent_of[r1] = r2
                self.__size[r2] += self.__size[r1]
            else:
                self.__parent_of[r2] = r1
                self.__size[r1] += self.__size[r2]
                if self.__rank_of[r1] == self.__rank_of[r2]:
                    self.__rank_of[r1] += 1

    def is_same(self, a, b):
        return self.__root(a) == self.__root(b)

    def size(self, a):
        return self.__size[self.__root(a)]

    def groups(self):
        groups = {}
        for k in self.__parent_of.keys():
            r = self.__root(k)
            if r not in groups:
                groups[r] = []
            groups[r].append(k)
        return [groups[x] for x in groups]


def main():
    N, M = map(int, input().split())
    E = [tuple(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        uft = UnionFindTree(list(range(1, N+1)))
        for j in range(M):
            if i == j:
                continue
            a, b = E[j]
            uft.unite(a, b)
        if uft.size(1) != N:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
