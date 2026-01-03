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
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
def main():
    n = int(input())
    uf = UnionFind(n)
    xs = [None]*n
    ys = [None]*n
    ps = [None]*n
    for i in range(n):
        x, y = map(int, input().split())
        ps[i] = [x, y]
        xs[i] = [x, i]
        ys[i] = [y, i]
    xs.sort()
    ys.sort()
    dist_xs = [None]*(n-1)
    dist_ys = [None]*(n-1)
    for i in range(n-1):
        dist_xs[i] = [xs[i+1][0] - xs[i][0], xs[i+1][1], xs[i][1]]
        dist_ys[i] = [ys[i+1][0] - ys[i][0], ys[i+1][1], ys[i][1]]
    dist_xs.sort()
    dist_ys.sort()
    x_i, y_i = 0, 0
    ans = 0
    while x_i < len(dist_xs) or y_i < len(dist_ys):
        if x_i < len(dist_xs) and y_i < len(dist_ys):
            if dist_xs[x_i][0] < dist_ys[y_i][0]:
                if not uf.same(dist_xs[x_i][1], dist_xs[x_i][2]):
                    uf.union(dist_xs[x_i][1], dist_xs[x_i][2])
                    ans += dist_xs[x_i][0]
                x_i += 1
            else:
                if not uf.same(dist_ys[y_i][1], dist_ys[y_i][2]):
                    uf.union(dist_ys[y_i][1], dist_ys[y_i][2])
                    ans += dist_ys[y_i][0]
                y_i += 1
        elif x_i < len(dist_xs):
            if not uf.same(dist_xs[x_i][1], dist_xs[x_i][2]):
                uf.union(dist_xs[x_i][1], dist_xs[x_i][2])
                ans += dist_xs[x_i][0]
            x_i += 1
        else:
            if not uf.same(dist_ys[y_i][1], dist_ys[y_i][2]):
                uf.union(dist_ys[y_i][1], dist_ys[y_i][2])
                ans += dist_ys[y_i][0]
            y_i += 1
    print(ans)

if __name__ == "__main__":
    main()