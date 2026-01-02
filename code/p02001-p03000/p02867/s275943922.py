# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_c

class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
    def find(self, x):
        if self.data[x] < 0:
            return x
        else:
            self.data[x] = self.find(self.data[x])
            return self.data[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.data[y] < self.data[x]:
                x, y = y, x
            self.data[x] += self.data[y]
            self.data[y] = x
        return (x != y)
    def same(self, x, y):
        return (self.find(x) == self.find(y))
    def size(self, x):
        return -self.data[self.find(x)]

N, *AB = map(int, open(0).read().split())
A, B = AB[:N], AB[N:]

AI = sorted((a, i) for i, (b, a) in enumerate(sorted(zip(B, A))))

A.sort()
B.sort()

if any(a > b for a, b in zip(A, B)):
    print("No")
    quit()

uf = UnionFind(N)
for j, (a, i) in enumerate(AI):
    uf.union(i, j)

if uf.size(0) != N or any(a <= b for a, b in zip(A[1:], B)):
    print("Yes")
else:
    print("No")