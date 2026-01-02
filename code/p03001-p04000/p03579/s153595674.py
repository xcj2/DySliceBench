class UnionFindTree():
    def __init__(self, N):
        self.__parent_of = [None] * N
        self.__rank_of = [0] * N
        self.__size = [1] * N

    def root(self, value):
        if self.__parent_of[value] is None:
            return value
        else:
            self.__parent_of[value] = self.root(self.__parent_of[value])
            return self.__parent_of[value]

    def unite(self, a, b):
        r1 = self.root(a)
        r2 = self.root(b)
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
        return self.root(a) == self.root(b)

    def size(self, a):
        return self.__size[self.root(a)]

    def groups(self):
        groups = {}
        for k in range(len(self.__parent_of)):
            r = self.root(k)
            if r not in groups:
                groups[r] = []
            groups[r].append(k)
        return [groups[x] for x in groups]


def main():
    N, M = map(int, input().split())
    adj = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        adj[A-1].add(B-1)
        adj[B-1].add(A-1)
    uft = UnionFindTree(N)
    for i in range(N):
        adji = list(adj[i])
        x = adji[0]
        for y in adji[1:]:
            uft.unite(x, y)
    groups = uft.groups()
    if len(groups) == 1:
        print(N * (N-1) // 2 - M)
    else:
        print(len(groups[0]) * len(groups[1]) - M)


if __name__ == "__main__":
    main()
