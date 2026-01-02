import sys
def input():
    return sys.stdin.readline()[:-1]

class UnionFind:
    def __init__(self, N):
        self.roots = list(range(N + 1))
        self.counter = [1] * (N + 1)

    def get_root(self, n):
        if self.roots[n] != n:
            self.roots[n] = self.get_root(self.roots[n])
        return self.roots[n]

    def union(self, a, b):
        a, b = sorted([self.get_root(a), self.get_root(b)])
        if a != b:
            self.roots[b] = a
            self.counter[a] += self.counter[b]
            self.counter[b] = 0

    def find(self, a, b):
        return self.get_root(a) == self.get_root(b)

    def count(self, x):
        return (self.counter[self.get_root(x)])

def resolve():
    N, M, K = [int(x) for x in input().split()]
    list = [[] for _ in range(N)]
    block = [[] for _ in range(N)]

    uf = UnionFind(N)

    for _ in range(M):
        A, B = [int(x)-1 for x in input().split()]
        list[A].append(B)
        list[B].append(A)
        uf.union(A,B)

    for _ in range(K):
        C, D = [int(x)-1 for x in input().split()]
        block[C].append(D)
        block[D].append(C)

    for i in range(N):
        ans = uf.count(i) - len(list[i]) - 1
        for j in block[i]:
            if uf.find(i ,j):
                ans -= 1

        print(ans, end=" ")

resolve()