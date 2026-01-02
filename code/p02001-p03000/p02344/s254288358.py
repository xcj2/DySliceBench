import sys 
input = sys.stdin.readline


class UnionFindWeighted:
    """ポテンシャル付きUnionFind"""
    def __init__(self, n):
        self.parent = [-1] * n
        self.weight = [0] * n
        self.cnt = n
        self.INF = 10 ** 18
       
    def root(self, x):
        """頂点xの根を求める"""
        if self.parent[x] < 0:
            return x
        rt = self.root(self.parent[x])
        self.weight[x] += self.weight[self.parent[x]]
        self.parent[x] = rt
        return rt

    def merge(self, x, y, weight):
        """頂点xを含む集合と頂点y含む集合を結合する
        weight: 頂点yに対する頂点xのポテンシャル(頂点xの方がweight高い)
        """
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        if self.parent[root_x] < self.parent[root_y]:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
            self.weight[root_y] = -weight + self.weight[x] - self.weight[y]
        else:
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y
            self.weight[root_x] = weight - self.weight[x] + self.weight[y]
        self.cnt -= 1

    def is_same(self, x, y):
        """頂点x, yが同じ集合に属するかどうかを返す"""
        return self.root(x) == self.root(y)

    def diff(self, x, y):
        """頂点yに対する頂点xのポテンシャルを求める
        ただし、頂点x,y間にポテンシャルが定義されていない場合は INF を返す
        """
        if not self.is_same(x, y):
            return self.INF
        return self.weight[x] - self.weight[y]

    def get_size(self, x):
        """頂点xを含む集合の要素数を返す"""
        return -self.parent[self.root(x)]

    def get_cnt(self):
        """集合の個数を返す"""
        return self.cnt


def solve():
    n, q = list(map(int, input().split()))
    query = [list(map(int, input().split())) for i in range(q)]
    INF = 10 ** 18
    ufw = UnionFindWeighted(n)

    for i in range(q):
        if query[i][0] == 0:
            # クエリ1の場合
            _, x, y, weight = query[i]
            ufw.merge(x, y, weight)
        else:
            # クエリ2の場合
            _, x, y = query[i]
            ans = ufw.diff(x, y)
            if ans == INF:
                print("?")
            else:
                print(ans)


if __name__ == "__main__":
    solve()
