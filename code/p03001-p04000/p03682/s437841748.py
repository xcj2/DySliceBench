import sys
input = sys.stdin.readline
from heapq import heappop, heappush

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N = int(input())
    X = []
    Y = []
    for i, _ in enumerate(range(N)):
        x, y = map(int, input().split())
        X.append((x, i))
        Y.append((y, i))
    X.sort()
    Y.sort()
    hq = []
    for i in range(N-1):
        x1, x1_ind = X[i]
        x2, x2_ind = X[i+1]
        y1, y1_ind = Y[i]
        y2, y2_ind = Y[i+1]
        heappush(hq, (x2-x1, x1_ind, x2_ind))
        heappush(hq, (y2-y1, y1_ind, y2_ind))
    ans = 0
    union_find = UnionFind(N)
    while hq:
        w, s, t = heappop(hq)
        if not union_find.is_same(s, t):
            union_find.union(s, t)
            ans += w

    print(ans)

if __name__ == '__main__':
    main()