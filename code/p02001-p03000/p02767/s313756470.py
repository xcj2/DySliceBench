import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([1, 4]), 5)

    def test_2(self):
        self.assertEqual(think([14, 14, 2, 13, 56, 2, 37]), 2354)


def solve():
    x = read()
    result = think(x)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


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


def think(x):
    left = min(x)
    right = max(x)
    min_cost = 1e20
    for p in range(left, right + 1):
        min_cost = min(min_cost, calc_cost(x, p))
    return min_cost


def write(result):
    print(result)


def calc_cost(x, p):
    return sum(map(lambda x: abs(x - p) ** 2, x))


if __name__ == '__main__':
    # unittest.main()
    solve()