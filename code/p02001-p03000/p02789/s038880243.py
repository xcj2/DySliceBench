import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(3, 3), 'Yes')

    def test_2(self):
        self.assertEqual(think(3, 2), 'No')


def solve():
    n, m = read()
    result = think(n, m)
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


def think(n, m):
    if n == m:
        return 'Yes'
    return 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()