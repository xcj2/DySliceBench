import sys
import heapq
input = sys.stdin.readline
N = int(input())
XYI = sorted([[int(_) for _ in input().split()] + [_] for _ in range(N)])
visited = [False] * N
H = []
for j in range(N - 1):
    heapq.heappush(H, (XYI[j + 1][0] - XYI[j][0], XYI[j][2], XYI[j + 1][2]))
XYI.sort(key=lambda xs: xs[1])
for j in range(N - 1):
    heapq.heappush(H, (XYI[j + 1][1] - XYI[j][1], XYI[j + 1][2], XYI[j][2]))
ans = 0

UF = list(range(N + 1))
SIZE = [0] + [1] * N  # 1-indexed


def find(x):
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]


def unite(x, y):
    if not is_same(x, y):
        X, Y = find(x), find(y)
        SX, SY = SIZE[X], SIZE[Y]
        if SX > SY:
            m = UF[X] = Y
        else:
            m = UF[Y] = X
        SIZE[m] = SX + SY
        SIZE[X + Y - m] = 0


def is_same(x, y):
    return find(x) == find(y)


def scan_uf():
    for i in range(len(UF)):
        find(i)


while H:
    d, i1, i2 = heapq.heappop(H)
    if not is_same(i1, i2):
        unite(i1, i2)
        ans += d
print(ans)
