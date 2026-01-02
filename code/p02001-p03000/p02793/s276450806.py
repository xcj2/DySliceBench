import unittest
import functools


class TestE(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([2, 3, 4]), 13)

    def test_2(self):
        self.assertEqual(think([12, 12, 12, 12, 12]), 5)

    def test_3(self):
        self.assertEqual(think([1000000, 999999, 999998]), 996989508)

    def test_4(self):
        self.assertEqual(gcd(3, 2), 1)


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


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


def think(a):
    mode = 10 ** 9 + 7

    lcm_of_all_a = functools.reduce(lambda x, y: lcm(x, y), a, 1)
    lcm_of_all_a %= mode   # THIS LINE IS KEY POINT

    b = map(lambda x: lcm_of_all_a * inverse(x, mode) % mode, a)
    return sum(b) % mode


def write(result):
    print(result)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd(a, b):
    if a < b:
        return gcd(b, a)

    while True:
        if a % b == 0:
            return b
        a, b = b, a % b


def inverse(x, mode):
    return pow(x, mode - 2, mode)


if __name__ == '__main__':
    # unittest.main()
    solve()