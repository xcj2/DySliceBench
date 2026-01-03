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


x_max, y_max, N = il()
x_min, y_min = 0, 0
s = 0
for i in range(N):
    x, y, a = il()
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    else:
        y_max = min(y_max, y)
if x_min > x_max or y_min > y_max:
    print(0)
else:
    print((x_max - x_min) * (y_max - y_min))
