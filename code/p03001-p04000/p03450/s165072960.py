class UnionFindTree:
    def __init__(self, size):
        self.parent = list(range(size))
        self.dist = [0]*size

    def find_root(self, x):
        if self.parent[x] == x:
            return x, 0
        else:
            self.parent[x], d = self.find_root(self.parent[x])
            self.dist[x] += d
            return self.parent[x], self.dist[x]

    def union(self, x, y, d):
        r1, d1 = self.find_root(x)
        r2, d2 = self.find_root(y)

        if r1 != r2:
            self.parent[r2] = r1
            self.dist[r2] = (d1 - d2) + d
        else:
            if (d2 - d1) != d:
                return False

        return True

def main():
    (N, M) = tuple(map(int, input().split(' ')))

    tree = UnionFindTree(N)

    for i in range(M):
        l, r, d = map(int, input().split(' '))

        if not tree.union(l-1, r-1, d):
            print('No')
            return

    print('Yes')

main()
