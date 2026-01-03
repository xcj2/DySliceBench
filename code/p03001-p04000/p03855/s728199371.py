class UnionFindTree():
    def __init__(self, values=[]):
        self.__parent_of = {}
        self.__rank_of = {}
        for value in values:
            self.add(value)

    def add(self, value):
        if value in self.__parent_of:
            raise RuntimeError("Dupulicated Value Added")
        self.__parent_of[value] = None
        self.__rank_of[value] = 0

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
            else:
                self.__parent_of[r2] = r1
                if self.__rank_of[r1] == self.__rank_of[r2]:
                    self.__rank_of[r1] += 1


def main():
    N, K, L = map(int, input().split())
    uft = UnionFindTree(range(N))
    for _ in range(K):
        p, q = map(int, input().split())
        uft.unite(p-1, q-1)
    uft2 = UnionFindTree(range(N))
    for _ in range(L):
        r, s = map(int, input().split())
        uft2.unite(r-1, s-1)
    pair = [(0, 0)] * N
    cnt = {}
    for i in range(N):
        p = (uft.root(i), uft2.root(i))
        if p not in cnt:
            cnt[p] = 0
        cnt[p] += 1
        pair[i] = p
    ans = [0] * N
    for i in range(N):
        ans[i] = cnt[pair[i]]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
