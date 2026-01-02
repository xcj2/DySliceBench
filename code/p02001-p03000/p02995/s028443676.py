from decimal import Decimal, ROUND_FLOOR


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def divisible_count(a, b, d):
    a = Decimal(str(a))
    b = Decimal(str(b))
    d = Decimal(str(d))

    x = (b / d).quantize(Decimal("0"), rounding=ROUND_FLOOR)
    y = ((a - 1) / d).quantize(Decimal("0"), rounding=ROUND_FLOOR)
    return int(x - y)


A, B, C, D = map(int, input().split())

x = divisible_count(A, B, C)
y = divisible_count(A, B, D)
z = divisible_count(A, B, lcm(C, D))

print(B - A + 1 - (x + y - z))
