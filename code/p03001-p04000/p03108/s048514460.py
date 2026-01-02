class UnionFind:
    def __init__(self, size: int):
        self.parent = [-1 for _ in range(size)]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size(px) > self.size(py):
            px, py = py, px
        self.parent[py] += self.parent[px]
        self.parent[px] = py
        return

    def find(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def size(self, x):
        return -self.parent[self.find(x)]

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main():
    # input
    N, M = map(int, input().split())
    A, B = [], []

    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)

    # solve
    # ref: http://drken1215.hatenablog.com/entry/2019/03/03/224600
    # ref: https://atcoder.jp/contests/abc120/submissions/4450601
    uf = UnionFind(N)
    ans = [N*(N-1)//2]
    for i in range(M-1, 0, -1):
        p1 = uf.find(A[i])
        p2 = uf.find(B[i])
        if p1 != p2:
            ans.append(ans[-1] - uf.size(p1)*uf.size(p2))
        else:
            ans.append(ans[-1])
        uf.unite(p1, p2)
    return ans


print(*list(reversed(main())), sep="\n")
