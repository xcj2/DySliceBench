import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.n = n + 1
        self.parents = [-1] * (n + 1)
        self.mem = [[] for _ in range(n+1)]

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

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def members(self, x):
        root = self.find(x)
        if not self.mem[root]:
            self.mem[root] = [i for i in range(1, self.n) if self.find(i) == root]
        return self.mem[root]

def main():
    N, M, K = map(int, input().split())

    friends = defaultdict(lambda : 1)
    friendsGroup = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        friendsGroup.union(a, b)
        friends[a] += 1
        friends[b] += 1

    block_and_same = defaultdict(int)
    for _ in range(K):
        c, d = map(int, input().split())
        if friendsGroup.same(c, d):
            block_and_same[c] += 1
            block_and_same[d] += 1

    ans = [0] * (N + 1)
    for i in range(1, N+1):
        ans[i] = friendsGroup.size(i) - friends[i] - block_and_same[i]
    print(*ans[1:])

if __name__ == '__main__':
    main()
