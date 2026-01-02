import unittest
import functools


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4, 1, 3), 7)

    def test_2(self):
        self.assertEqual(think(1000000000, 141421, 173205), 34076506)


def solve():
    n, a, b = read()
    result = think(n, a, b)
    write(result)


def read():
    return read_int(3)


def read_int(n):
    return read_type(int, n, sep=' ')


def read_float(n):
    return read_type(float, n, sep=' ')


def read_type(t, n, sep):
    return list(map(lambda x: t(x), read_line().split(sep)))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n, a, b):
    mode = 10 ** 9 + 7

    result = pow(2, n, mode) - 1
    if result < 0:
        result += mode
    result -= combi(n, a, mode)
    if result < 0:
        result += mode
    result -= combi(n, b, mode)
    if result < 0:
        result += mode
    return result


def write(result):
    print(result)


def combi(n, a, mode):
    numer = functools.reduce(lambda x, y: (x * y) % mode, range(n, n - a, -1))
    denom = functools.reduce(lambda x, y: (x * y) % mode, range(1, a + 1))
    return (numer * pow(denom, mode - 2, mode)) % mode


def fact(n, mode=None):
    result = 1
    for i in range(1, n + 1):
        result *= i
        if mode:
            result %= mode
    return result


if __name__ == '__main__':
    # unittest.main()
    solve()