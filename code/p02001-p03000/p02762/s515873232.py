class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

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
        return (i for i in range(self.N) if self.find(i) == root)

    def roots(self):
        return (i for i, x in enumerate(self.parents) if x < 0)

    def group_count(self):
        return len(list(self.roots()))

    def all_group_members(self):
        dic = {}
        for x in range(self.N):
            r = self.find(x)
            dic.setdefault(r, [])
            dic[r].append(x)
        return dic

def main():
    N,M,K=map(int, input().split())
    AB=[tuple(map(int, input().split())) for _ in range(M)]
    CD=[tuple(map(int, input().split())) for _ in range(K)]
    UF=UnionFind(N)
    X=[0]*N
    for a,b in AB:
        UF.union(a-1,b-1)
    for i in range(N):
        X[i] += UF.size(i)-1
    for a,b in AB:
        X[a-1]-=1
        X[b-1]-=1
    for c,d in CD:
        if UF.same(c-1,d-1):
            X[c-1]-=1
            X[d-1]-=1
    print(*X)

if __name__ == "__main__":
    main()