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


def main():
    n,m=map(int,input().split())
    l=[list(map(int,input().split())) for _ in range(m)]
    l.reverse()
    res = [(n*(n-1))//2]
    u = UnionFind(n)
    for sl in l:
        a = sl[0]-1
        b = sl[1]-1
        if u.find(a) == u.find(b):
            res.append(res[-1])
        else:
            res.append(res[-1] - u.size(a) * u.size(b))
            u.union(a,b)
    res.pop()
    res.reverse()
    print("\n".join(map(str,res)))
main()