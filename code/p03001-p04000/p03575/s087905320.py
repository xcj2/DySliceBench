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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


def main():
    n, m = map(int, input().split())
    a, b = [], []
    for i in range(m):
        A, B = map(int, input().split())
        a.append(A - 1)
        b.append(B - 1)
    
    ans = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i == j:
                continue
            uf.union(a[j], b[j])
        if uf.group_count() != 1:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    main()