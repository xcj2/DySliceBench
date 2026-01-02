import sys


def is_a(m: int, f: int) -> bool:
    if 80 <= m + f:
        return True
    return False


def is_b(m: int, f: int) -> bool:
    if 65 <= m + f < 80:
        return True
    return False


def is_c(m: int, f: int, r: int) -> bool:
    if 50 <= r:
        return True
    if 50 <= m + f < 65:
        return True
    return False


def is_d(m: int, f: int, r: int) -> bool:
    if 30 <= m + f < 50:
        if 50 <= r:
            return False
        return True
    return False


def rank(m: int, f: int, r: int) -> str:
    if -1 in [m, f]:
        return 'F'

    if m < 0:
        m = 0
    if f < 0:
        f = 0
    if r < 0:
        r = 0

    if is_d(m, f, r):
        return 'D'
    if is_c(m, f, r):
        return 'C'
    if is_b(m, f):
        return 'B'
    if is_a(m, f):
        return 'A'
    return 'F'


def resolve():
    for line in sys.stdin:
        m, f, r = map(int, line.split())

        if m == f == r == -1:
            break

        print(rank(m, f, r))


resolve()

