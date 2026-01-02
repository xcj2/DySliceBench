import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think([10, 30, 40, 20]),
            30
        )

    def test_2(self):
        self.assertEqual(
            think([10, 10]),
            0
        )

    def test_3(self):
        self.assertEqual(
            think([30, 10, 60, 10, 60, 50]),
            40
        )


def solve():
    h = read()
    result = think(h)
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


def think(h):
    n_max = 10 ** 5
    h_max = 10 ** 4

    dp = [h_max * n_max for i in range(len(h))]
    dp[0] = 0
    dp[1] = abs(h[0] - h[1])

    for i in range(2, len(h)):
        dp[i] = min(
                    abs(h[i] - h[i - 1]) + dp[i - 1],
                    abs(h[i] - h[i - 2]) + dp[i - 2]
                )

    return dp[len(h) - 1]


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()