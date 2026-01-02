def solve():
    from collections import Counter
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    ABs = [tuple(map(int, input().split())) for _ in range(M)]
    CDs = [tuple(map(int, input().split())) for _ in range(K)]

    # Union-Findデータ構造
    class UnionFind:
        def __init__(self, numV):
            self.pars = list(range(numV))
            self.ranks = [0] * numV
        def find(self, x):
            if self.pars[x] == x: return x
            else:
                self.pars[x] = self.find(self.pars[x])
                return self.pars[x]
        def union(self, x, y):
            x, y = self.find(x), self.find(y)
            if x == y: return
            if self.ranks[x] < self.ranks[y]:
                self.pars[x] = y
            else:
                self.pars[y] = x
                if self.ranks[x] == self.ranks[y]:
                    self.ranks[x] += 1
        def same(self, x, y):
            return self.find(x) == self.find(y)

    UF = UnionFind(N)
    for A, B in ABs:
        A, B = A-1, B-1
        UF.union(A, B)

    for i in range(N):
        UF.find(i)

    cnt = Counter(UF.pars)
#    print('cnt:', cnt)

    anss = [cnt[UF.pars[i]]-1 for i in range(N)]
#    print('anss:', anss)

    for A, B in ABs:
        A, B = A-1, B-1
        if UF.same(A, B):
            anss[A] -= 1
            anss[B] -= 1
    for C, D in CDs:
        C, D = C-1, D-1
        if UF.same(C, D):
            anss[C] -= 1
            anss[D] -= 1

    print(' '.join(map(str, anss)))


solve()
