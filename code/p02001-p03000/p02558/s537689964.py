import sys
input = sys.stdin.readline


def solve():
    N, q = map(int, input().split())
    root = [-1] * N
    rank = [0] * N

    def find(x: int) -> int:
        if root[x] < 0:
            return x
        else:
            while root[x] >= 0:
                x = root[x]
            return x

    def union(x: int, y: int):
        x = find(x)
        y = find(y)
        if x == y:
            return
        elif rank[x] > rank[y]:
            root[x] += root[y]
            root[y] = x
        else:
            root[y] += root[x]
            root[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    for _ in range(q):
        t, u, v = map(int, input().split())
        if t:
            print(int(find(u) == find(v)))
        else:
            union(u, v)


solve()
