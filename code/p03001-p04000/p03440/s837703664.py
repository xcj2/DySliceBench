import heapq
from collections import defaultdict
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


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
    N, M = map(int, input().split())

    A = list(map(int, input().split()))

    uf = UF_tree(N)
    for _ in range(M):
        x, y = map(int, input().split())
        uf.unite(x, y)

    d = defaultdict(list)
    for i in range(N):
        heapq.heappush(d[uf.find(i)], A[i])

    if M == N - 1:
        print(0)
        exit()
    elif N < 2 * (N - M - 1):
        print("Impossible")
        exit()

    nodes = 2 * (N - M - 1)
    ans = 0
    tmp = []
    for k, v in d.items():
        ans += heapq.heappop(v)
        tmp.extend(v)
        nodes -= 1

    tmp.sort()
    ans += sum(tmp[:nodes])
    print(ans)
