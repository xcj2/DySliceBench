import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([4, 2, 5, 1, 3]), 3)

    def test_2(self):
        self.assertEqual(think([4, 3, 2, 1]), 4)

    def test_3(self):
        self.assertEqual(think([1, 2, 3, 4, 5, 6]), 1)

    def test_4(self):
        self.assertEqual(think([5, 7, 4, 2, 6, 8, 1, 3]), 4)

    def test_5(self):
        self.assertEqual(think([1]), 1)


def solve():
    p = read()
    result = think(p)
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


def think(p):
    dp = [0 for _ in range(len(p) + 1)]
    count = 1
    dp[1] = p[0]
    for i in range(1, len(p)):
        if p[i] <= dp[i]:
            count += 1
            dp[i + 1] = p[i]
        else:
            dp[i + 1] = dp[i]
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()