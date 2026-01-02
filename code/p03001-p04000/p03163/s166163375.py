import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(8, [[3, 30], [4, 50], [5, 60]]),
            90
        )

    def test_2(self):
        self.assertEqual(
            think(
                5, [
                    [1, 1000000000], [1, 1000000000], [1, 1000000000],
                    [1, 1000000000], [1, 1000000000]
                ]
            ),
            5000000000
        )

    def test_3(self):
        self.assertEqual(
            think(15, [[6, 5], [5, 6], [6, 4], [6, 6], [3, 5], [7, 2]]),
            17
        )


def solve():
    w, list_of_w_and_v = read()
    result = think(w, list_of_w_and_v)
    write(result)


def read():
    n, w = read_int(2)
    list_of_w_and_v = []
    for _ in range(n):
        list_of_w_and_v.append(read_int(2))
    return w, list_of_w_and_v


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


def think(w, list_of_w_and_v):
    invalid = -1

    # dp[weight] = max value at 'weight'
    dp = [invalid for _ in range(w + 1)]
    dp[0] = 0

    for weight, value in list_of_w_and_v:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == invalid:
                continue
            if i + weight >= len(dp):
                continue
            dp[i + weight] = max(
                    dp[i + weight],
                    dp[i] + value
            )
    return max(dp)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()