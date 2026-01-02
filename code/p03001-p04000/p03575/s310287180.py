class UnionFind:

    def __init__(self, size):
        self.table = [i for i in range(size)]

    def find(self, x):
        return self.table[x]

    def union(self, x, y):
        x1 = self.find(x)
        y1 = self.find(y)
        if x1 == y1: return False
        # 併合
        for i in range(len(self.table)):
            if self.table[i] == y1:
                self.table[i] = x1
        return True


def solve():
    [N, M] = [int(x) for x in input().split()]

    edges = []
    g = [[False] * N for _ in range(N)]
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        edges.append((a-1, b-1))
        g[a-1][b-1] = g[b-1][a-1] = True

    ans = 0
    for i in range(len(edges)):
        uf = UnionFind(N)

        for j in range(len(edges)):
            e = edges[j]
            if i == j:
                # print("Remove {} -> {}".format(*e))
                continue
            uf.union(*e)

        n = len(set(uf.table))
        ans += n != 1

        # print(uf.table)
        # print(len(set(uf.table)))
        # print(any(uf.table))
    return ans


def main():
    print(solve())


if __name__ == '__main__':
    main()


