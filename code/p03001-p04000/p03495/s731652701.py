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


N, K = il()
A = il()
d = {}
c = 0
for a in A:
    try:
        d[a] += 1
    except KeyError:
        d[a] = 1
k = K - len(d)
if k >= 0:
    print(0)
    exit()
sd = sorted(d.items(), reverse=True, key=lambda x: x[1])
s = 0
for _, v in sd[k:]:
    s += v
print(s)
