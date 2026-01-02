class UnionFindTree:
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x


def main():
    n, q = map(int, input().split())
    union_find = UnionFindTree(n)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            union_find.union(x, y)
        else:
            x_p = union_find.find(x)
            y_p = union_find.find(y)
            if x_p == y_p:
                print(1)
            else:
                print(0)


if __name__ == "__main__":
    main()

