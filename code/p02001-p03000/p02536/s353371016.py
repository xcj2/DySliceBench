from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())
class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def root(self, x):
        if(self.parents[x] < 0):
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def unite(self, x, y) -> bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        return True

    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents[1:]) if x < 0]

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

def main():
    N, M = i_map()
    u = UnionFind(N)
    for _ in range(M):
        A, B = i_map()
        u.unite(A, B)
    ans = len(u.roots()) - 1
    print(ans)

if __name__ == "__main__":
    main()
