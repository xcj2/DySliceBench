class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # root検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


from collections import deque

def solve():
    N, K, L = tuple(map(int, input().split()))

    PQ = []
    for _ in range(K):
        PQ.append(tuple(map(int, input().split())))
    RS = []
    for _ in range(L):
        RS.append(tuple(map(int, input().split())))

    # print(N, K, L)
    # print(PQ)
    # print(RS)

    road = UnionFind(10**5*2 + 1)
    rail = UnionFind(10**5*2 + 1)

    for a, b in PQ:
        road.union(a, b)

    for a, b in RS:
        rail.union(a, b)

    d = {}
    for i in range(N):
        i += 1
        road_root = road.find(i)
        rail_root = rail.find(i)
        if not (road_root, rail_root) in d:
            d[(road_root, rail_root)] = 1
        else:
            d[(road_root, rail_root)] += 1

    ans = deque()
    for i in range(N):
        i += 1
        road_root = road.find(i)
        rail_root = rail.find(i)
        ans.append(d[(road_root, rail_root)])

    return " ".join(tuple(map(str, ans)))


if __name__ == '__main__':
    res = solve()
    print(res)
