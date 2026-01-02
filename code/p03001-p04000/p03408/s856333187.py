import sys


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


N = ii()
s = {}
for _ in range(N):
    tmp = ii(str)
    try:
        s[tmp] += 1
    except KeyError:
        s[tmp] = 1

M = ii()
for _ in range(M):
    tmp = ii(str)
    try:
        s[tmp] -= 1
    except KeyError:
        s[tmp] = 0
print(max(max(s.values()), 0))
