import unittest


class TestE(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(12), 1)

    def test_2(self):
        self.assertEqual(think(5), 0)

    def test_3(self):
        self.assertEqual(think(1000000000000000000), 124999999999999995)


def solve():
    n = read()
    result = think(n)
    write(result)


def read():
    return read_int(1)[0]


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


def think(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return 0
    return count_fives(n // 2)


def write(result):
    print(result)


def count_fives(n):
    count = 0
    mode = 5
    while mode <= n:
        count += n // mode
        mode *= 5
    return count


if __name__ == '__main__':
    # unittest.main()
    solve()
