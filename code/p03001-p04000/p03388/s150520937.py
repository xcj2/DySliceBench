from math import ceil, floor

q = int(input())
ab = [list(map(int, input().split())) for _ in range(q)]


def f(a, b, x):
    return (a + x - 1) * (b - x + 1)


def get_mx(a, b, num):
    tmp = (b - a + 2) / 2
    lx = max(1, floor(tmp))
    rx = min(num, ceil(tmp))
    mx = max(f(a, b, lx), f(a, b, rx))
    return mx


def check(a, b, num):
    mx = 1
    a, b = min(a, b), max(a, b)
    if num < a:
        mx = max(mx, get_mx(1, num, num))
    elif a <= num < b:
        mx = max(mx, get_mx(1, num, a - 1))
        mx = max(mx, get_mx(a + 1, num - a + 1, num - a + 1))
    elif num >= b:
        if num - b + 1 > a - 1:
            mx = max(mx, get_mx(1, num + 1, a - 1))
            mx = max(mx, get_mx(a + 1, num - a - 2, num - a - b + 2))
            mx = max(mx, get_mx(num - b - 2, b - 1, b - 1))
        elif num - b + 1 == a - 1:
            mx = max(mx, get_mx(1, num + 1, a - 1))
            mx = max(mx, get_mx(a + 1, b - 1, b - 1))
        else:
            mx = max(mx, get_mx(1, num + 1, num - b + 1))
            mx = max(mx, get_mx(num - b + 2, b - 1, a + b - num - 2))
            mx = max(mx, get_mx(a + 1, num - a + 1, num - a + 1))

    if mx < a * b:
        return True

    return False


for a, b in ab:
    if a == b:
        print(2 * a - 2)
        continue
    l = 0
    r = 10 ** 10
    while r - l > 1:
        m = (l + r) // 2
        if check(a, b, m):
            l = m
        else:
            r = m

    print(l)
