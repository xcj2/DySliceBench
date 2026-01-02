import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 3, 1, 2), [3, 0])

    def test_2(self):
        self.assertEqual(think(2, 2, 1, 1), [2, 1])


def solve():
    w, h, x, y = read()
    result = think(w, h, x, y)
    write(result)


def read():
    return read_int(4)


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


def think(w, h, x, y):
    area = calc_smaller_area(w, h)
    multiple_ways_exist = can_be_multiple_ways(w, h, x, y)
    return [area, 1 if multiple_ways_exist else 0]


def write(result):
    print('{0:f} {1:d}'.format(result[0], result[1]))


def calc_smaller_area(w, h):
    return w * h / 2.0


def can_be_multiple_ways(w, h, x, y):
    return x == w / 2.0 and y == h / 2.0


if __name__ == '__main__':
    # unittest.main()
    solve()