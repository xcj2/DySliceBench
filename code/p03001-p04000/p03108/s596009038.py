class UnionFindTree():
    def __init__(self, values=[]):
        self.parent_of = {}
        self.rank_of = {}
        self.cnt = {}
        for value in values:
            self.add(value)

    def add(self, value):
        if value in self.parent_of:
            raise RuntimeError("Dupulicated Value Added")
        self.parent_of[value] = None
        self.rank_of[value] = 0
        self.cnt[value] = 1

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
                self.cnt[r2] += self.cnt[r1]
            else:
                self.parent_of[r2] = r1
                self.cnt[r1] += self.cnt[r2]
                if self.rank_of[r1] == self.rank_of[r2]:
                    self.rank_of[r1] += 1

    def is_same(self, a, b):
        return self.__root(a) == self.__root(b)

    def count_group(self, a):
        return self.cnt[self.__root(a)]


def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    uft = UnionFindTree(list(range(1, N+1)))
    prev = N*(N-1)//2
    answers = [prev]
    for i in range(M):
        a, b = bridges[i]
        if not uft.is_same(a, b):
            prev -= uft.count_group(a) * uft.count_group(b)
        uft.unite(a, b)
        answers.append(prev)
    answers.reverse()
    for i in range(1, M+1):
        print(answers[i])


if __name__ == "__main__":
    main()
