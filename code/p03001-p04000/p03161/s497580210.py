import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(3, [10, 30, 40, 50, 20]),
            30
        )

    def test_2(self):
        self.assertEqual(
            think(1, [10, 20, 10]),
            20
        )

    def test_3(self):
        self.assertEqual(
              think(100, [10, 10]),
              0
        )

    def test_4(self):
        self.assertEqual(
              think(4, [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]),
              40
        )


def solve():
    k, h = read()
    result = think(k, h)
    write(result)


def read():
    n, k = read_int(2)
    return k, read_int(n)


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


def think(k, h):
    n_max = 10 ** 5
    h_max = 10 ** 4

    dp = [h_max * n_max for _ in range(len(h))]
    dp[0] = 0
    for i in range(1, len(dp)):
        for j in range(1, k + 1):
            if i - j < 0:
                break
            dp[i] = min(
                        dp[i],
                        dp[i - j] + abs(h[i] - h[i - j])
                    )
    return dp[len(h) - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()