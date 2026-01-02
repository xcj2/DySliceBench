import math
def P(n, r):
    return math.factorial(n)//math.factorial(n-r)
def C(n, r):
    return P(n, r)//math.factorial(r)
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
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M = map(int, input().split())
uf = UnionFind(N)
query = [list(map(int, input().split())) for _ in range(M)]
ans = C(N,2)
ans_arr = [0]*M
ans_arr[M-1] = ans
for i in range(M-1):
    A, B = query[M-1-i][0]-1, query[M-1-i][1]-1
    if not uf.same(A,B):
        ans -= uf.size(A) * uf.size(B)
    ans_arr[M-2-i] = ans
    uf.union(A,B)
for i in ans_arr:
    print(i)