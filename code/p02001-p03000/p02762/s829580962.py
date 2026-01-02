import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)

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

def main():
    N, M, K = map(int, input().split())

    friends = defaultdict(lambda : 1)
    friendsGroup = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        friendsGroup.union(a, b)
        friends[a] += 1
        friends[b] += 1

    blocks = defaultdict(int)
    for _ in range(K):
        c, d = map(int, input().split())
        if friendsGroup.same(c, d):
            blocks[c] += 1
            blocks[d] += 1

    ans = [friendsGroup.size(i) - friends[i] - blocks[i] for i in range(1, N+1)]
    print(*ans)

if __name__ == '__main__':
    main()
