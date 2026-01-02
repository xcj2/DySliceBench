import itertools
import sys
sys.setrecursionlimit(5000)


class TestInput:
    @classmethod
    def input(self):
        TestInput.current += 1
        return TestInput.data.splitlines()[TestInput.current]
    current = -1
    data = '''\
2 2
0 1
1 0
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
0 0
'''


def read_input():
    # return TestInput.input()
    return input()


class IslandMap:
    moves = list(itertools.product([-1, 0, 1], [-1, 0, 1]))

    def __init__(self, w, h, c):
        self.w = w
        self.h = h
        self.c = c

    def dfs(self, p):
        self.c[p[0]][p[1]] = 0
        for m in IslandMap.moves:
            n = (p[0] + m[0], p[1] + m[1])
            if 0 <= n[0] < self.h and 0 <= n[1] < self.w:
                if self.c[n[0]][n[1]] == 1:
                    self.dfs(n)

    def solve(self):
        region = 0
        lattice = itertools.product(range(self.h), range(self.w))
        for p in lattice:
            if self.c[p[0]][p[1]] == 1:
                self.dfs(p)
                region += 1
        return region


while True:
    w, h = map(int, read_input().split())
    if w == 0 or h == 0:
        break
    c = [list(map(int, read_input().split())) for i in range(h)]
    island = IslandMap(w, h, c)
    print(island.solve())

