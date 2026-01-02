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


def dense(a, b):
    try:
        return 100 * b / (a + b)
    except ZeroDivisionError:
        return 0


A, B, C, D, E, F = il()
A *= 100
B *= 100
max_dense = 0
max_water = 0
max_sugar = 0
for a in range(31):
    for b in range(31):
        water = a * A + b * B
        if water == 0:
            break
        for c in range((F - water) // C + 1):
            for d in range((F - water) // D + 1):
                sugar = c * C + d * D
                if water + sugar > F or water / 100 * E < sugar:
                    break
                if max_dense <= dense(water, sugar):
                    max_dense = dense(water, sugar)
                    max_water = water
                    max_sugar = sugar
print(max_water + max_sugar, max_sugar)
