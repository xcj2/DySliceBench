#template
def inputlist(): return [int(k) for k in input().split()]
#template
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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


N,M = inputlist()
li = [0]*M
for i in range(M):
    A,B = inputlist()
    A-=1
    B-=1
    li[i] = [A,B]
ans = [N*(N-1)//2]
uf = UnionFind(N)
for i in range(M-1,-1,-1):
    A,B = li[i][0],li[i][1]
    if uf.same(A,B):
        ans.append(ans[-1])
        continue
    tmp = ans[-1]-uf.size(A)*uf.size(B)
    ans.append(tmp)
    uf.union(A,B)
for i in range(M-1,-1,-1):
    print(ans[i])