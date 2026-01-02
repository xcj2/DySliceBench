N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(M)]

UF = list(range(N + 1))
SIZE = [0] + [1] * N  # 1-indexed


def find(x):
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]


def unite(x, y):
    X, Y = find(x), find(y)
    SX, SY = SIZE[X], SIZE[Y]
    if SX > SY:
        m = X
    else:
        m = Y
    SIZE[m] = SX + SY
    SIZE[X + Y - m] = 0
    UF[X + Y - m] = m


def is_same(x, y):
    return find(x) == find(y)


def scan_uf():
    for i in range(len(UF)):
        find(i)


ans = [N * (N - 1) // 2]
for a, b in AB[::-1]:
    if not is_same(a, b):
        ans += [ans[-1] - SIZE[find(a)] * SIZE[find(b)]]
        unite(a, b)
    else:
        ans += [ans[-1]]
print(*ans[-2::-1], sep='\n')
