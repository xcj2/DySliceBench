from collections import defaultdict
import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
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

def main():
    N, K, L = map(int, input().split())
    road = UnionFind(N)
    train = UnionFind(N)
    for _ in range(K):
        p, q = map(int, input().split())
        p -= 1
        q -= 1
        road.union(p,q)
    for _ in range(L):
        r, s = map(int, input().split())
        r -= 1
        s -= 1
        train.union(r,s)

    d = defaultdict(int)
    for i in range(N):
        a = road.find(i)
        b = train.find(i)
        d[(a,b)] += 1

    ans = [0] * N

    for i in range(N):
        a = road.find(i)
        b = train.find(i)
        ans[i] = d[(a,b)]
    print(*ans)




if __name__ == "__main__":
    main()