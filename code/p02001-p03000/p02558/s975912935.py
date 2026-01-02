# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from typing import Iterable
import sys
def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    uf = UnionFindTree(N)
    ans = []
    for _ in range(Q):
        t, u, v = map(int, input().split())
        if t:
            ans.append('1' if uf.same(u, v) else '0')
        else:
            uf.union(u, v)
    print('\n'.join(ans))

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

if __name__ == '__main__':
    main()
