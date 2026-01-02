import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(1, 3, 4), 4)

    def test_2(self):
        self.assertEqual(think(3, 2, 3), 5)


def solve():
    p, q, r = read()
    result = think(p, q, r)
    write(result)


def read():
    return read_int(3)


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


def think(p, q, r):
    return min(p + q, q + r, r + p)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()