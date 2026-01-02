import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(25), 17)

    def test_2(self):
        self.assertEqual(think(1), 1)

    def test_3(self):
        self.assertEqual(think(100), 108)

    def test_4(self):
        self.assertEqual(think(2020), 40812)

    def test_5(self):
        self.assertEqual(think(200000), 400000008)


def solve():
    n = read()
    result = think(n)
    write(result)


def read():
    return read_int(1)[0]


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


def think(n):
    count = 0
    dp = [[0 for last_digit in range(10)] for first_digit in range(10)]
    for i in range(1, n + 1):
        first_digit = first_digit_of(i)
        last_digit = last_digit_of(i)
        dp[first_digit][last_digit] += 1
    for first_digit in range(10):
        for last_digit in range(10):
            count += dp[first_digit][last_digit] * dp[last_digit][first_digit]
    return count


def write(result):
    print(result)


def first_digit_of(a):
    return int(str(a)[0])


def last_digit_of(a):
    return int(str(a)[-1])


if __name__ == '__main__':
    # unittest.main()
    solve()