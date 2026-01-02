import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(5, 7, 5), 'Yes')

    def test_2(self):
        self.assertEqual(think(4, 4, 4), 'No')

    def test_3(self):
        self.assertEqual(think(4, 9, 6), 'No')

    def test_4(self):
        self.assertEqual(think(3, 3, 4), 'Yes')


def solve():
    a, b, c = read()
    result = think(a, b, c)
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


def think(a, b, c):
    s = set()
    s.add(a)
    s.add(b)
    s.add(c)
    return 'Yes' if len(s) == 2 else 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()