n, m = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))
xy = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

parents = [i for i in range(n)]
ranks = [0 for _ in range(n)]


def root(x):
    return x if x == parents[x] else root(parents[x])


def is_same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return
    if ranks[x] < ranks[y]:
        parents[x] = y
        if ranks[x] == ranks[y]:
            ranks[y] += 1
    else:
        parents[y] = x
        if ranks[x] == ranks[y]:
            ranks[x] += 1


for x_, y_ in xy:
    unite(x_, y_)

cnt = sum((1 if is_same(i, p_) else 0) for i, p_ in enumerate(p))
print(cnt)
