import sys
def main():
    input = sys.stdin.readline

    N, M, K=map(int, input().split())
    friend_or_block = [set() for _ in range(N)]
    friends_chain = UnionFindTree(N)

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        friends_chain.union(a, b)
        friend_or_block[a].add(b)
        friend_or_block[b].add(a)

    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if friends_chain.same(c, d):
            friend_or_block[c].add(d)
            friend_or_block[d].add(c)

    print(*[friends_chain.size(i) - len(friend_or_block[i]) - 1 for i in range(N)])

class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        while p[x] >= 0: x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y: return
        if p[x] > p[y]: x, y = y, x
        p[x], p[y] = p[x] + p[y], x

    def same(self, x, y): return self.find(x) == self.find(y)
    def size(self, x): return -self.parent[self.find(x)]

if __name__ == '__main__':
    main()

