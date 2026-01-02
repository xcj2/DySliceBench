def main():
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    ans = [0] * n
    for _ in range(m):
        A, B = map(int, input().split())
        A, B = A - 1, B - 1
        uf.union(A, B)
        ans[A] -= 1
        ans[B] -= 1

    for i in range(n):
        ans[i] = ans[i] + uf.size(i) - 1

    for _ in range(k):
        C, D = map(int, input().split())
        C, D = C - 1, D - 1
        if uf.same(C, D):
            ans[C] -= 1
            ans[D] -= 1
    
    print(*ans)
    
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

if __name__ == '__main__':
    main()