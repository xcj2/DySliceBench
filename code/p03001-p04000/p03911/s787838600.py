# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, M, KL):
    uf = UnionFindTree(N + M)
    for i, (K, *L) in enumerate(KL):
        for l in L:
            uf.union(i, N + l - 1)
    g = uf.find(0)
    for i in range(1, N):
        if uf.find(i) != g:
            break
    else:
        print('YES')
        return
    print('NO')

class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        while p[x] >= 0: x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y: return False
        if p[x] > p[y]: x, y = y, x
        p[x], p[y] = p[x] + p[y], x
        return True

    def same(self, x, y): return self.find(x) == self.find(y)
    def size(self, x): return -self.parent[self.find(x)]

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    KL = [list(map(int, input().split())) for _ in range(N)]
    main(N, M, KL)
