import sys
input = sys.stdin.readline


def solve():
    N, q = map(int, input().split())
    root = [-1] * N

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
        if root[x] > root[y]:
            x, y = y, x
        root[x] += root[y]
        root[y] = x

    for _ in range(q):
        t, u, v = map(int, input().split())
        if t:
            print(int(find(u) == find(v)))
        else:
            union(u, v)


solve()
