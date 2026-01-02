import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([5, 4, 2, 1], 1), 'Yes')

    def test_2(self):
        self.assertEqual(think([380, 19, 1], 2), 'No')

    def test_3(self):
        self.assertEqual(think([4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789], 3), 'Yes')


def solve():
    a, m = read()
    result = think(a, m)
    write(result)


def read():
    n, m = read_int(2)
    return read_int(n), m


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


def think(a, m):
    total = sum(a)
    threshold = total // (4 * m) if total % (4 * m) == 0 else total // (4 * m) + 1
    return 'Yes' if len(list(filter(lambda x: x >= threshold, a))) >= m else 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()