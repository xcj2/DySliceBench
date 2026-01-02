import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([1, 2, 3]), (3, 1, 2))

    def test_2(self):
        self.assertEqual(think([100, 100, 100]), (100, 100, 100))

    def test_3(self):
        self.assertEqual(think([41, 59, 31]), (31, 41, 59))


def solve():
    xyz = read()
    result = think(xyz)
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


def think(xyz):
    return xyz[2], xyz[0], xyz[1]


def write(result):
    print('{0:d} {1:d} {2:d}'.format(result[0], result[1], result[2]))


if __name__ == '__main__':
    # unittest.main()
    solve()