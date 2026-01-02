import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4, 3), '3333')

    def test_2(self):
        self.assertEqual(think(7, 7), '7777777')


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
    s_a, s_b = str(a), str(b)
    canditate_a = str(a) * b
    canditate_b = str(b) * a
    return min(canditate_a, canditate_b)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()