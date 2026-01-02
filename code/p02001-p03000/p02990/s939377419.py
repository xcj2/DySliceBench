from math import factorial


def perm(n, r):
    return factorial(n) // factorial(n - r)


def comb(n, r):
    return perm(n, r) // factorial(r)


def ball_spliting_variations(n, i):
    if i == 1:
        return 1
    return comb(n - 1, i - 1)


def inserting_variations(n, i):
    n -= i - 1
    if n < 0:
        return 0
    return comb(n + i, i)


DIV = (10 ** 9) + 7
n, k = map(int, input().split())
blue, red = k, n - k
for i in range(1, k + 1):
    ball = ball_spliting_variations(blue, i)
    inst = inserting_variations(red, i)
    print((ball * inst) % DIV)
