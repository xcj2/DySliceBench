import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(1, [4, 1, 5]), 5)

    def test_2(self):
        self.assertEqual(think(9, [7, 9, 3, 2, 3, 8, 4, 6]), 0)

    def test_3(self):
        self.assertEqual(think(0, [1000000000, 1000000000, 1000000000]), 3000000000)


def solve():
    k, h = read()
    result = think(k, h)
    write(result)


def read():
    n, k = read_int(2)
    return k, read_int(n)


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


def think(k, h):
    if k >= len(h):
        return 0
    h.sort(key=lambda x: -x)
    h[0:k] = [0] * k
    return sum(h)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()