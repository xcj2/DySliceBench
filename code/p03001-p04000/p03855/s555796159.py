import sys
sys.setrecursionlimit(4100000)
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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, K, L = map(int,input().split())
    road = UnionFind(N)
    train = UnionFind(N)

    for k in range(K):
        p, q = map(int,input().split())
        p -= 1
        q -= 1
        road.union(p,q)

    for k in range(L):
        r, s = map(int,input().split())
        r -= 1
        s -= 1
        train.union(r,s)


    D = dict()
    P = [0]*N
    for k in range(N):
        t = (10**6)*(train.find(k)+1)+road.find(k)
        P[k] = t
        if t in D:
            D[t] += 1
        else:
            D[t] = 1
    ans = []
    for k in range(N):
        ans.append(D[P[k]])
    print(*ans)


if __name__ == '__main__':
    main()
