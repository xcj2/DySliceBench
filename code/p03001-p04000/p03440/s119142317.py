from heapq import heappush, heappop, heapify


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
    A = list(map(int, input().split()))
    uft = UnionFindTree(N)
    for _ in range(M):
        x, y = map(int, input().split())
        uft.unite(x, y)
    groups = uft.groups()
    if len(groups) == 1:
        print(0)
        return
    ans = 0
    h = []
    for g in groups:
        costs = [A[x] for x in g]
        costs.sort()
        ans += costs[0]
        for cost in costs[1:]:
            heappush(h, cost)
    if len(groups) == 2 and N == 2:
        print(ans)
        return
    if len(h) < len(groups)-2:
        print("Impossible")
        return
    for _ in range(len(groups)-2):
        ans += heappop(h)
    print(ans)


if __name__ == "__main__":
    main()
