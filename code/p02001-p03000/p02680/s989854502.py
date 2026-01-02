#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float("inf")


class UnionFind(object):
    def __init__(self, N):
        self.tree = [-1]*N

    def root(self, i):
        if self.tree[i] < 0:
            return i
        else:
            self.tree[i] = self.root(self.tree[i])
            return self.tree[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.tree[y] < self.tree[x]:
                x, y = y, x
            self.tree[x] += self.tree[y]
            self.tree[y] = x
        return x == y


def main():
    # 1. 座圧します
    # 2. 座標ごとに線分が乗っているかどうかを示す配列を作ります
    # 3. 面ごとに同じ領域内かどうか、グルーピングします
    # 4. 牛と同じグループの面積を数え上げます

    # 入力
    N, M = map(int, readline().split())
    x_coord, y_coord = {-INF, 0, INF}, {-INF, 0, INF}
    A, B, C = [0]*N, [0]*N, [0]*N
    for i in range(N):
        a, b, c = map(int, readline().split())
        A[i], B[i], C[i] = a, b, c
        x_coord.add(a)
        x_coord.add(b)
        y_coord.add(c)
    D, E, F = [0]*M, [0]*M, [0]*M
    for i in range(M):
        d, e, f = map(int, readline().split())
        D[i], E[i], F[i] = d, e, f
        x_coord.add(d)
        y_coord.add(e)
        y_coord.add(f)

    # 1. 座圧
    mx = list(sorted(x_coord))
    my = list(sorted(y_coord))
    invx, invy = {}, {}
    for i, x in enumerate(mx):
        invx[x] = i
    for i, y in enumerate(my):
        invy[y] = i
    H = len(my)
    W = len(mx)

    # 2. 線分ごとに線分が乗っているかどうかを示す配列を作ります(imos法)
    # segx[i][j]は座標(i, j)と(i+1, j)をつなぐ線分
    # segy[i][j]は座標(i, j)と(i, j+1)をつなぐ線分
    segx = [[0]*H for _ in range(W)]
    segy = [[0]*H for _ in range(W)]

    for a, b, c in zip(A, B, C):
        segx[invx[a]][invy[c]-1] += 1
        segx[invx[b]][invy[c]-1] -= 1
    for i in range(W-1):
        for j in range(H):
            segx[i+1][j] += segx[i][j]

    for d, e, f in zip(D, E, F):
        segy[invx[d]-1][invy[e]] += 1
        segy[invx[d]-1][invy[f]] -= 1
    for i in range(W):
        for j in range(H-1):
            segy[i][j+1] += segy[i][j]

    # 3. 面ごとに同じ領域内かどうか、グルーピングします
    # UnionFindで検査していく
    uf = UnionFind(W*H)

    # segx[i][j]は座標(i, j)と(i+1, j)をつなぐ線分であり
    # 面[i][j-1]と面[i][j]の境界にあたる
    # segy[i][j]は座標(i, j)と(i, j+1)をつなぐ線分であり
    # 面[i-1][j]と面[i][j]の境界にあたる
    for i in range(W):
        for j in range(H):
            if i+1 < W and segy[i][j] == 0:
                uf.unite(i+j*W, i+1+j*W)
            if j+1 < H and segx[i][j] == 0:
                uf.unite(i+(j+1)*W, i+j*W)

    # 4. 牛と同じグループの面積を数え上げます
    # 無限の彼方と同じグル-プなら、INF
    ushi = invx[0]+invy[0]*W
    if uf.same(ushi, 0):
        print("INF")
        return

    area = 0
    for i in range(W-1):
        for j in range(H-1):
            if uf.same(ushi, i+j*W):
                area += (mx[i+1]-mx[i])*(my[j+1]-my[j])
    print(area)
    return


if __name__ == '__main__':
    main()
