import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parent = [i for i in range(n_nodes)]
        self.rank = [1] * n_nodes
        self.size = [1] * n_nodes

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_parent_list(self):
        return [i for i in range(self.n_nodes) if self.find(i) == i]

    def get_n_groups(self):
        return len(self.get_parent_list())

    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def main():
    N, M = map(int, input().split())
    Bridge = [list(map(int, input().split())) for _ in range(M)]
    answer = [N * (N - 1) // 2]
    UF = UnionFind(N)
    for i in range(M):
        AB = Bridge[M - i - 1]
        A = AB[0] - 1
        B = AB[1] - 1
        if UF.check(A, B):
            last = answer[-1]
            answer.append(last)
            continue
        else:
            before = UF.size[UF.find(A)]
            UF.unite(AB[0] - 1, AB[1] - 1)
            after = UF.size[UF.find(A)]
            last = answer[-1]
            if before == after:
                answer.append(last)
            else:
                answer.append(last - (after - before) * before)

    answer = answer[::-1]
    print(*answer[1:], sep="\n")


if __name__ == "__main__":
    main()
