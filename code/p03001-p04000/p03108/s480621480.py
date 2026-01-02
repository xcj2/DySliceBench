# ABC 120 D

from collections import deque

class UnionFind():
    # n : 要素数
    def __init__(self, n):
        self.n = n
        # root[x] < 0 ならそのノードが根かつその値が木の要素数
        # root[x] > 0 ならそのノードが根
        self.root = [-1] * (n+1)
        # 木の高さの管理
        self.rnk = [0] * (n+1)

    # x が所属するグループの根を返す
    def findRoot(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.findRoot(self.root[x])  # 経路圧縮
            return self.root[x]

    # x と y がそれぞれ所属するグループを結合する
    def unite(self, x, y):
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            # 既に同じグループに所属していれば何もしない
            return
        elif self.rnk[x] > self.rnk[y]:    # x の方が高さがある場合
            self.root[x] += self.root[y]   # x の要素数に y の要素数を足す
            self.root[y] = x               # y の親を x にする
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

    def count(self, x):
        return -self.root[self.findRoot(x)]

def resolve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    AB = AB[::-1]

    ret = []

    uf = UnionFind(N)

    for a, b in AB:
        if uf.isSameGroup(a-1, b-1):
            ret.append(0)
        else:
            ret.append(uf.count(a-1) * uf.count(b-1))
            uf.unite(a-1, b-1)

    ans = 0
    for i in range(M-1, -1, -1):
        ans += ret[i]
        print(ans)

if __name__ == "__main__":
    resolve()
