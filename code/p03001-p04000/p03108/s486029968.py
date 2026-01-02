class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
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

def main():
    N, M = map(int, input().split())
    B = [tuple(map(int, input().split())) for _ in range(M)]
    U = UnionFind(N)
    t = N * (N - 1) // 2
    R = [t]
    for a, b in reversed(B):
        a, b = a - 1, b - 1
        if U.find(a) != U.find(b):
            t -= U.size(a) * U.size(b)
            U.union(a, b)
        R.append(t)
    R.pop()
    print('\n'.join(str(i) for i in reversed(R)))
            
main()
