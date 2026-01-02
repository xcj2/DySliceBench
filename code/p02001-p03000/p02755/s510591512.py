import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 2), 25)

    def test_2(self):
        self.assertEqual(think(8, 10), 100)

    def test_3(self):
        self.assertEqual(think(19, 99), -1)


def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    return read_int(2)


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


def think(a, b):
    max_a = 100
    min_tax = 0.08
    ceil = int(max_a / min_tax) + 1
    for c in range(1, ceil + 1):
        tax_a = int(c * 0.08)
        tax_b = int(c * 0.10)
        if a == tax_a and b == tax_b:
            return c
    return -1


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()