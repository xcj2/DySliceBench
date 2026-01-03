class UnionFind:
    def __init__(self, n: int):
        self.__n = n
        self.__par = list(range(self.__n))
        self.__size = [1 for _ in range(self.__n)]

    def root(self, x: int) -> int:
        if self.__par[x] == x:
            return x
        self.__par[x] = self.root(self.__par[x])
        return self.__par[x]

    def merge(self, x: int, y: int) -> bool:
        rx, ry = self.root(x), self.root(y)
        if rx == ry: return False

        if self.__size[rx] < self.__size[ry]:
            rx, ry = ry, rx

        self.__size[rx] += self.__size[ry]
        self.__par[ry] = rx
        return True

    def check(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def size(self, x: int) -> int:
        return self.__size[self.root(x)]


from collections import defaultdict

N, K, L = map(int, input().split())
rail_uf = UnionFind(N + 1)
road_uf = UnionFind(N + 1)

for _ in range(K):
    p, q = map(int, input().split())
    rail_uf.merge(p, q)

for _ in range(L):
    r, s = map(int, input().split())
    road_uf.merge(r, s)

d = defaultdict(int)
for i in range(1, N + 1):
    tup = (rail_uf.root(i), road_uf.root(i))
    d[tup] += 1

ans = []
for i in range(1, N + 1):
    tup = (rail_uf.root(i), road_uf.root(i))
    ans.append(str(d[tup]))

print(" ".join(ans))
