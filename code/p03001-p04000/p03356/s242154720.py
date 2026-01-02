# http://www.geocities.jp/m_hiroi/light/pyalgo61.html
class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    # 部分集合とその要素数を返す
    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a
        
def solve(N, M, P, xy):
    uf = UnionFind(N + 1)
    for x, y in xy:
        uf.union(x, y)
    result = 0
    for i, n in enumerate(P):
        if uf.find(i + 1) == uf.find(n):
            result += 1
    return result

N, M = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
xy = [[int(x) for x in input().split()] for i in range(M)]

print(solve(N, M, P, xy))

