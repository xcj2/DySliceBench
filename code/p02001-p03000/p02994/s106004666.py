import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(5, 2), 18)

    def test_2(self):
        self.assertEqual(think(3, -1), 0)

    def test_3(self):
        self.assertEqual(think(30, -50), -1044)


def solve():
    n, l = read()
    result = think(n, l)
    write(result)


def read():
    return read_int(2)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n, l):
    a = [l + i - 1 for i in range(1, n + 1)]
    original_sum = sum(a)
    buf = []
    for i, e in enumerate(a):
        buf.append((abs(e), i))
    buf.sort(key=lambda x: x[0])
    return original_sum - a[buf[0][1]]


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()