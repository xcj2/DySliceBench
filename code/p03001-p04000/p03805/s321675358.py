N, M = map(int, input().split())
E = [[] for _ in range(N)]
dp = {}

for _ in range(M):
    a, b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

S = 1
G = (1 << N) - 1


def is_visited(v: int, path: int):
    return path & (1 << v)


def visit(v: int, path: int):
    return path ^ (1 << v)


def count(u: int, path: int):
    if path == G:
        return 1

    if (u, path) in dp:
        return dp[(u, path)]

    return sum(
        count(v, visit(v, path))
        for v in E[u]
        if not is_visited(v, path)
    )


print(count(0, S))
