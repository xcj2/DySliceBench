import sys
def main():
    input = sys.stdin.readline
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

    N, M, K=map(int, input().split())
    friend_or_block = [0] * N
    friends_chain = UnionFindTree(N)

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        friends_chain.union(a, b)
        friend_or_block[a] += 1
        friend_or_block[b] += 1

    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if friends_chain.same(c, d):
            friend_or_block[c] += 1
            friend_or_block[d] += 1

    print(*[friends_chain.size(i) - friend_or_block[i] - 1 for i in range(N)])

if __name__ == '__main__':
    main()

