class UnionFind:#「貼るだけ」
    from typing import List, Set

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def merge(self, x, y) -> int:
        x = self.leader(x)
        y = self.leader(y)

        if x == y:
            return 0

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return self.parent[x]

    def same(self, x, y) -> bool:
        return self.leader(x) == self.leader(y)

    def leader(self, x) -> int:
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.leader(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        return -self.parent[self.leader(x)]

    def groups(self) -> List[Set[int]]:
        groups = dict()

        for i in range(self.n):
            p = self.leader(i)
            if not groups.get(p):
                groups[p] = set()
            groups[p].add(i)

        return list(groups.values())

def main():
    N,M = map(int, input().split())

    uf = UnionFind(N)

    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        uf.merge(A,B)

    print(len(uf.groups()) - 1)


if __name__ == '__main__':
    main()