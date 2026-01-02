import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(10, [4, 5, 6]), 'Yes')

    def test_2(self):
        self.assertEqual(think(20, [4, 5, 6]), 'No')

    def test_3(self):
        self.assertEqual(think(210, [31, 41, 59, 26, 53]), 'Yes')

    def test_4(self):
        self.assertEqual(think(211, [31, 41, 59, 26, 53]), 'No')


def solve():
    h, a = read()
    result = think(h, a)
    write(result)


def read():
    h, n = read_int(2)
    return h, read_int(n)


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


def think(h, a):
    return 'Yes' if sum(a) >= h else 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()