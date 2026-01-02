# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from typing import Iterable
import sys
def main(N, M, K, AB, CD):
    friend_chain = UnionFindTree(N)
    friend_count = [0] * N
    block_count = [0] * N
    for a, b in AB:
        a, b = a - 1, b - 1
        friend_chain.union(a, b)
        friend_count[a] += 1
        friend_count[b] += 1
    for c, d in CD:
        c, d = c - 1, d - 1
        if friend_chain.same(c, d):
            block_count[c] += 1
            block_count[d] += 1
    print(*[friend_chain.size(i) - 1 - friend_count[i] - block_count[i] for i in range(N)])

class UnionFindTree:
    def __init__(self, n: int) -> None:
        self.parent = [-1] * n

    def find(self, x: int) -> int:
        p = self.parent
        while p[x] >= 0: x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y: return False
        if p[x] > p[y]: x, y = y, x
        p[x], p[y] = p[x] + p[y], x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -self.parent[self.find(x)]

    def same_all(self, indices: Iterable[int]) -> bool:
        f, v = self.find, self.find(indices[0])
        return all(f(i) == v for i in indices)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    main(N, M, K, AB, CD)
