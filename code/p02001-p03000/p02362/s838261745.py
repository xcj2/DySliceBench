# グラフクラスとベルマンフォードクラスの定義
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n+1)]

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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n + 1) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


class Graph():
    def __init__(self, N, Type):
        self._V = N  # 頂点の数
        self._E = 0  # 辺の数
        self.type = Type
        if Type == "D":
            # 2次元リスト
            self.G = [[] for i in range(self._V+1)]
        elif Type == "W":
            # 隣接行列
            self.G = [[float("inf") for i in range(self._V+1)]
                      for j in range(self._V+1)]
        elif Type == "B" or Type == "K":
            # 1次元リスト
            self.G = []

    def E(self):
        """ 辺数 """
        return self._E

    @property
    def V(self):
        """ 頂点数 """
        return self._V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self._E += 1
        if self.type == "D":
            self.G[_from].append((_to, _cost))

        elif self.type == "W":
            self.G[_from][_to] = _cost

        elif self.type == "B" or self.type == "K":
            self.G.append((_from, _to, _cost))

    def add_both(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する (無向グラフ) """
        self.add(_from, _to, _cost)
        self.add(_to, _from, _cost)


class Bellman_Ford(Graph):
    def __init__(self, N):
        super().__init__(N, "B")
        self.d = [float("inf")]*(self._V+1)

    def shortest_path(self, s):
        self.d[s] = 0
        for _ in range(self._V):
            flag = False
            for From, To, cost in self.G:
                newlen = self.d[From]+cost
                if newlen < self.d[To]:
                    flag = True
                    self.d[To] = newlen
            if not flag:
                break
        return self.d

    def have_negative_circle(self, s):
        self.d[s] = 0
        for i in range(1, self._V+1):
            flag = False
            for From, To, cost in self.G:
                newlen = self.d[From]+cost
                if newlen < self.d[To]:
                    flag = True
                    self.d[To] = newlen
            if not flag:
                break
            if i == self._V:
                return False
        return self.d


def main():
    V, E, r = map(int, input().split())
    r+=1
    # ベルマンフォードクラスのインスタンスを定義
    G = Bellman_Ford(V)
    for i in range(E):
        s, t, d = map(int, input().split())
        s+=1
        t+=1
        G.add(s,t,d)
    result = G.have_negative_circle(r)
    if result==False:
        print("NEGATIVE CYCLE")
        return
    else:
        for i in range(1, V+1):
            if result[i] == float("inf"):
                print("INF")
            else:
                print(result[i])
        return

if __name__ == "__main__":
    main()
