import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 3), 6)

    def test_2(self):
        self.assertEqual(think(123, 456), 18696)

    def test_3(self):
        self.assertEqual(think(100000, 99999), 9999900000)


def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    return read_int(2)


def read_int(n):
    return read_type(int, n)


def read_float(n):
    return read_type(float, n)


def read_type(t, n):
    return list(map(lambda x: t(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b):
    return lcm(a, b)


def write(result):
    print(result)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == '__main__':
    # unittest.main()
    solve()
