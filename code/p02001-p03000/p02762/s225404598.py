from collections import defaultdict
import sys
input = sys.stdin.buffer.readline


class UF_tree:
    def __init__(self, n):
        self.root = [-1] * (n + 1)  # -1ならそのノードが根,で絶対値が木の要素数
        self.rank = [0] * (n + 1)

    def find(self, x):  # xの根となる要素番号を返す
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def getNodeLen(self, x):
        return -self.root[self.find(x)]


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    friend = UF_tree(N)
    d = defaultdict(int)

    for _ in range(M):
        A, B = map(int, input().split())
        friend.unite(A, B)
        d[A] += 1
        d[B] += 1

    for _ in range(K):
        C, D = map(int, input().split())
        if friend.isSame(C, D):
            d[C] += 1
            d[D] += 1

    ans = [friend.getNodeLen(i) - d[i] - 1 for i in range(1, N + 1)]
    print(*ans)
