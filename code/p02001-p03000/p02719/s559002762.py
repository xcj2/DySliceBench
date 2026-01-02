import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(7, 4), 1)

    def test_2(self):
        self.assertEqual(think(2, 6), 2)

    def test_3(self):
        self.assertEqual(think(1000000000000000000, 1), 0)


def solve():
    n, k = read()
    result = think(n, k)
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


def think(n, k):
    if n % k == 0:
        return 0
    m = n % k
    return min(m, abs(k - m))


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()