# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from typing import Iterable, List
import sys
def main(N, M, AB):
    uf = UnionFindTree(N)
    for a, b in AB:
        a, b = a - 1, b - 1
        uf.union(a, b)
    print(len(uf.groups()) - 1)

class UnionFindTree:
    __slots__ = ('parent')

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

    def groups(self) -> List[int]:
        return [i for i, p in enumerate(self.parent) if p < 0]

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    main(N, M, AB)
