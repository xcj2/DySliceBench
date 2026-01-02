import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.length = [1 for _ in range(n)] 

    def makeSet(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.length = [1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
            self.length[y] += self.length[x]
        else:
            self.parents[y] = x
            self.length[x] += self.length[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def getLength(self, x):
        x = self.find(x)
        return self.length[x]        

    def isSameGroup(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n, m = map(int, readline().split())
    uf = UnionFind(n)
    for _ in range(m):
        x, y, z = map(int, readline().split())
        x-=1
        y-=1
        uf.unite(x, y)
    s = set()
    for i in range(n):
        s.add(uf.find(i))
    print(len(s))
if __name__ == '__main__':
    main()
