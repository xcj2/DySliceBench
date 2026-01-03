import sys
input = sys.stdin.readline


class UnionFindTree():
    def __init__(self, N):
        self.N = N
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
        for k in range(self.N):
            r = self.root(k)
            if r not in groups:
                groups[r] = []
            groups[r].append(k)
        return [groups[x] for x in groups]


def main():
    N, M = map(int, input().split())
    uft = UnionFindTree(N)
    speakers = [[] for _ in range(M)]
    for i in range(N):
        langs = list(map(int, input().split()))
        for l in langs[1:]:
            speakers[l-1].append(i)
    for i in range(M):
        for j in range(1, len(speakers[i])):
            uft.unite(speakers[i][j-1], speakers[i][j])
    if len(uft.groups()) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
