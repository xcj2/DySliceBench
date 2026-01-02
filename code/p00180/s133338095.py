
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n+1)

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
        return [i for i in range(self.n+1) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def kr(edge,N):
    res = 0
    node = []
    G = UnionFind(N)
    for cost, p, q, in edge:
        if not G.same(p, q):
            G.union(p, q)
            res += cost
    return res

def solve():
    n,m=map(int,input().split())
    if n==0 and m==0:
        exit()
    edge=[]
    for _ in range(m):
        a,b,cost=map(int,input().split())
        edge.append((cost,a,b))
    edge.sort()
    ans=kr(edge,n)
    print(ans)
    return solve()
if __name__=="__main__":
  solve()

