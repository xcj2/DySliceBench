# 参考URL https://note.nkmk.me/python-union-find/
class UnionFind():
    # 各要素の親要素の番号を格納するリスト
    # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()
    
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    uf = UnionFind(n)
    for _ in range(m):
        i, j = map(int, input().split())
        uf.union(i-1, j-1)
    
    ans = 0
    for i in range(n):
        if uf.same(i, p[i]-1):
            ans += 1
    
    print(ans)

main()