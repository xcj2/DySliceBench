import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


def main():
    N, M = map(int, input().split())
    E = []
    for i in range(M):
        a, b = map(int, input().split())
        E.append((a-1, b-1))

    ans = 0
    # i 番目の辺を取り除いても、全ての頂点が連結しているか？
    # Union-Find で連結グラフか判定する
    for i in range(M):
        uf = UnionFind(N) # 最初、全ての頂点が非連結の状態
        for j in range(M):
            if i == j:
                pass # i 番目の辺を無視する
            else:
                # 要素が同じ集合にある＝頂点が連結している
                uf.union(E[j][0], E[j][1])
        # グラフ全体が連結なら、任意の頂点を含む集合のサイズが N のはず
        if uf.size(0) != N:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
