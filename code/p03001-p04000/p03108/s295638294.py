import sys
sys.setrecursionlimit(10 ** 7)


class UnionFind:
    def __init__(self, size: int):
        self.parent = [-1 for _ in range(size)]
        self.size = [1 for _ in range(size)]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.parent[px] > self.parent[py]:
                self.parent[py] = px
                self.parent[px] -= 1
                self.size[px] += self.size[py]
                self.size[py] = 0
            else:
                self.parent[px] = py
                self.parent[py] -= 1
                self.size[py] += self.size[px]
                self.size[px] = 0
        return

    def find(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main():
    # input
    N, M = map(int, input().split())
    brs = [list(map(int, input().split())) for _ in range(M)]

    # solve
    # ref: http://drken1215.hatenablog.com/entry/2019/03/03/224600
    # ref: https://atcoder.jp/contests/abc120/submissions/4450601
    uf = UnionFind(N)
    ans = [N*(N-1)//2]
    for i in range(M-1, 0, -1):
        a, b = brs[i][0], brs[i][1]
        a, b = a-1, b-1
        p1 = uf.find(a)
        p2 = uf.find(b)
        if p1 != p2:
            ans.append(ans[-1] - uf.size[p1]*uf.size[p2])
        else:
            ans.append(ans[-1])
        uf.unite(p1, p2)
    return ans


print(*list(reversed(main())), sep="\n")
