from collections import defaultdict

class UnionFind(object):

    def __init__(self, n):
        self.table = [-1] * N

    def find(self, x):
        parent = self.table[x] 
        if parent < 0:
            return x
        else:
            root = self.find(parent)
            self.table[x] = root
            return root

    def union(self, x1, x2):
        root1 = self.find(x1)
        root2 = self.find(x2)
        if root1 < root2:
            self.table[root1] += self.table[root2]
            self.table[root2] = root1
        else:
            self.table[root2] += self.table[root1]
            self.table[root1] = root2

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
xy = [[int(x) for x in input().split()] for i in range(M)]

def solve(N, M, A, xy):

    uf = UnionFind(N)
    for x, y in xy:
        uf.union(x, y)

    groups = defaultdict(list)
    for i in range(N):
        groups[uf.find(i)].append(A[i])

    groups = [sorted(g, reverse=True) for g in groups.values()]

    if len(groups) == 1:
        return 0

    r = 0

    xs = []
    for group in groups:
        r += group.pop()
        xs += group

    if len(groups) == 2:
        return r

    if len(groups) - 2 > len(xs):
        return "Impossible"

    xs.sort()
    r += sum(xs[:len(groups) - 2])

    return r

print(solve(N, M, A, xy))
