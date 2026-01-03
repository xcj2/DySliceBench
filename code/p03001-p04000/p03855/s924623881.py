import sys
from collections import defaultdict
input = sys.stdin.readline

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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

def main():
    n,k,l = map(int,input().split())
    Road = [list(map(int,input().split())) for i in range(k)]
    Train = [list(map(int,input().split())) for i in range(l)]

    uf_r = UnionFind(n)
    uf_t = UnionFind(n)

    for i in range(k):
        uf_r.union(Road[i][0]-1,Road[i][1]-1)

    for i in range(l):
        uf_t.union(Train[i][0]-1,Train[i][1]-1)

    Roots_dict = defaultdict(int)
    Roots = []
    for i in range(n):
        Roots.append(str(uf_r.find(i))+' '+str(uf_t.find(i)))
        Roots_dict[Roots[i]] += 1

    ans = [0]*n

    for i in range(n):
        ans[i] = Roots_dict[Roots[i]]

    print(*ans)

if __name__ == '__main__':
    main()