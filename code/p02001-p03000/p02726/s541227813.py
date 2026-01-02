import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(5, 2, 4), [5, 4, 1, 0])

    def test_2(self):
        self.assertEqual(think(3, 1, 3), [3, 0])

    def test_3(self):
        self.assertEqual(think(7, 3, 7), [7, 8, 4, 2, 0, 0])

    def test_4(self):
        self.assertEqual(think(10, 4, 8), [10, 12, 10, 8, 4, 1, 0, 0, 0])


def solve():
    n, x, y = read()
    result = think(n, x, y)
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


def think(n, x, y):
    result = [0] * n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            minimum_distance = min(j - i, 1 + abs(x - i) + abs(y - j))
            result[minimum_distance] += 1
    return result[1:]


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    # unittest.main()
    solve()