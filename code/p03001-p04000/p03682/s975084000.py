#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
               self.rank[x] += 1

class Kruskal:
    def __init__(self, Q, n):
        self.uf = UnionFind(n)
        self.cost = 0
        self.Q = Q
        for i in range(2 * (n - 1)):
            w, u, v = self.Q[i][0], self.Q[i][1], self.Q[i][2] 
            if self.uf.same_check(u, v) != True:
                self.uf.union(u, v)
                self.cost += w

#処理内容
def main():
    N = int(input())
    Lx = []
    Ly = []
    for i in range(N):
        x, y = getlist()
        Lx.append((x, i))
        Ly.append((y, i))
    Lx = sorted(Lx)
    Ly = sorted(Ly)
    Q = []

    for i in range(N - 1):
        u = Lx[i][1]
        v = Lx[i + 1][1]
        w = Lx[i + 1][0] - Lx[i][0]
        Q.append((w, u, v))
        u = Ly[i][1]
        v = Ly[i + 1][1]
        w = Ly[i + 1][0] - Ly[i][0]
        Q.append((w, u, v))
    Q = sorted(Q)
    Km = Kruskal(Q, N)
    print(Km.cost)

if __name__ == '__main__':
    main()