
def main():
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

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    n,m,k = map(int,input().split())
    uff = UnionFind(n)
    fr = [0]*n

    for i in range(m):
        a,b = map(int,input().split())
        uff.union(a-1,b-1)
        fr[a-1]+=1
        fr[b-1]+=1


    ans = [uff.size(i) -fr[i]-1 for i in range(n)]

    for i in range(k):
        c,d = map(int,input().split())
        if uff.same(c-1,d-1):
            ans[c-1] -=1
            ans[d-1] -=1
    print(*ans)
if __name__=="__main__":
    main()
