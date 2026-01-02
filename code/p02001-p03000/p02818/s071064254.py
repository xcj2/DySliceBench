import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 3, 3), (0, 2))

    def test_2(self):
        self.assertEqual(think(500000000000, 500000000000, 1000000000000), (0, 0))

    def test_3(self):
        self.assertEqual(think(1, 1, 10), (0, 0))


def solve():
    a, b, k = read()
    result = think(a, b, k)
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


def think(a, b, k):
    if a >= k:
        return a - k, b
    rem = k - a
    if b >= rem:
        return 0, b - rem
    else:
        return 0, 0


def write(result):
    print('{0:d} {1:d}'.format(result[0], result[1]))


if __name__ == '__main__':
    # unittest.main()
    solve()