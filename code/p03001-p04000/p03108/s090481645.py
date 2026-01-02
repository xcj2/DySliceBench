N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(M)]

UF = list(range(N + 1))
SIZE = [1] * (N + 1)


def find(x):
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]


def unite(x, y):
    m = min(find(x), find(y))
    SIZE[m] = SIZE[find(x)] + SIZE[find(y)]
    UF[find(x)] = m
    UF[find(y)] = m


def is_same(x, y):
    return find(x) == find(y)


ans = [N * (N - 1) // 2]
for a, b in AB[::-1]:
    if not is_same(a, b):
        ans += [ans[-1] - SIZE[find(a)] * SIZE[find(b)]]
        unite(a, b)
    else:
        ans += [ans[-1]]
print(*ans[M - 1::-1], sep='\n')
