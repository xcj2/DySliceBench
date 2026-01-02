class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        # xが根だったら自分自身をreturnする
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループかどうか
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


def main():
    N, M = map(int, input().split())

    A = [None] * M
    B = [None] * M

    for i in range(M):
        A[i], B[i] = map(int, input().split())

    uni = UnionFind(N)
    ans = [None] * M
    ans[M-1] = N * (N - 1) // 2
    for i in range(M - 1, 0, -1):
        x = A[i] - 1
        y = B[i] - 1
        # 辺でつなげても元々同じグループに属していた場合、変化はしない
        if uni.is_same(x, y):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - (uni.get_size(x) * uni.get_size(y))
        uni.union(x, y)


    for a in ans:
        print(a)

main()