import unittest


class TestE(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(8, [[3, 30], [4, 50], [5, 60]]),
            90
        )

    def test_2(self):
        self.assertEqual(
            think(1000000000, [[1000000000, 10]]),
            10
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
    w_max = 10 ** 9
    invalid = w_max + 1
    v_max = 10 ** 3
    n_max = 100

    # dp[value] = min weight at 'value'
    dp = [invalid for _ in range(v_max * n_max + 1)]
    dp[0] = 0

    for weight, value in list_of_w_and_v:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == invalid:
                continue
            if i + value >= len(dp):
                continue
            dp[i + value] = min(
                    dp[i + value],
                    dp[i] + weight
            )

    for i in range(len(dp) - 1, -1, -1):
        if dp[i] == invalid:
            continue
        if dp[i] > w:
            continue
        return i


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()