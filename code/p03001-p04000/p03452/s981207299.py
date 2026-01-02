import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


class WeightedUnionFind:
    def __init__(self, node: int) -> None:
        self.n = node
        self.par = [i for i in range(self.n)]
        self.rank = [0 for i in range(self.n)]
        self.diff_weight = [0 for i in range(self.n)]

    # ノードxのルートを求める
    def find(self, x: int) -> int:
        if x == self.par[x]:
            return x
        else:
            r = self.find(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return self.par[x]

    # ノードxのルートからの距離を求める
    def weight(self, x: int) -> int:
        self.find(x)
        return self.diff_weight[x]

    # weight(y) - weight(x) = w となるようにする
    def unite(self, x: int, y: int, w: int) -> bool:
        if self.isSame(x, y):
            # print("x and y has already united")
            return False

        w += self.weight(x)
        w -= self.weight(y)

        rx = self.find(x)
        ry = self.find(y)

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            w = -w

        self.par[ry] = self.par[rx]
        self.diff_weight[ry] = w

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True

    def isSame(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def diff(self, x: int, y: int) -> int:
        if self.isSame(x, y):
            return self.weight(y) - self.weight(x)
        else:
            raise ValueError("xとyは同じ木に属していません")


def judge(wuf, state):
    for l, r, d in state:
        if wuf.diff(l, r) != d:
            return False

    return True


n, m = li()
wuf = WeightedUnionFind(n)

lrd = []

for _ in range(m):
    l, r, d = li()
    l -= 1
    r -= 1

    lrd.append((l,r,d))

    wuf.unite(l, r, d)

print("Yes" if judge(wuf, lrd) else "No")