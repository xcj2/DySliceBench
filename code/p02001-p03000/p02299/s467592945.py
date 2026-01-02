def dot(a: complex, b: complex):
    return (a.conjugate() * b).real


def cross(a: complex, b: complex):
    return (a.conjugate() * b).imag


def is_contained(p: complex, g: list):
    flag = False

    for i in range(len(g)):
        a, b = g[i] - p, g[(i + 1) % len(g)] - p
        if a.imag > b.imag:
            a, b = b, a
        if a.imag <= 0 and 0 < b.imag:
            if cross(a, b) < 0:
                flag = not(flag)
        if cross(a, b) == 0 and dot(a, b) <= 0:
            return 1

    return 2 if flag else 0


n = int(input())
g = [complex(*map(int, input().split())) for _ in range(n)]
q = int(input())

for _ in range(q):
    p = complex(*map(int, input().split()))
    print(is_contained(p, g))

