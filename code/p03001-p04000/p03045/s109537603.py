class UnionFindTree:
    __slots__ = ('__tree', '__current')

    def __init__(self, n):
        self.__tree = [-1] * n
        self.__current = iter(self.__tree)

    def find(self, x):
        t = self.__tree
        if t[x] < 0:
            return x
        root = self.find(t[x])
        t[x] = root
        return root

    def union(self, x, y):
        t = self.__tree
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if t[x] > t[y]:
            x, y = y, x
        t[x] += t[y]
        t[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.__tree[self.find(x)]

    def __next__(self):
        try:
            return next(self.__current)
        except StopIteration:
            self.__current = iter(self.__tree)
            raise StopIteration()

    def __iter__(self):
        return self


def spline(func_=int, iter_=None):
    if iter_ is None:
        iter_ = input().split()
    return map(func_, iter_)


def main():
    n, m = spline()
    tree = UnionFindTree(n)
    for i in range(1, m + 1):
        x, y, _ = spline(func_=lambda x: int(x) - 1)
        tree.union(x, y)
    ans = 0
    for i in tree:
        if i < 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
