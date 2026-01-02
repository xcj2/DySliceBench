import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think([[10, 40, 70], [20, 50, 80], [30, 60, 90]]),
            210
        )

    def test_2(self):
        self.assertEqual(
            think([[100, 10, 1]]),
            100
        )

    def test_3(self):
        self.assertEqual(
            think([
                [6, 7, 8], [8, 8, 3], [2, 5, 2], [7, 8, 6],
                [4, 6, 8], [2, 3, 4], [7, 5, 1]
            ]),
            46
        )


def solve():
    list_of_abc = read()
    result = think(list_of_abc)
    write(result)


def read():
    n = read_int(1)[0]
    list_of_abc = []
    for _ in range(n):
        list_of_abc.append(read_int(3))
    return list_of_abc


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


def think(list_of_abc):
    n = len(list_of_abc)
    elems = len(list_of_abc[0])

    # dp[0 to n - 1][0 to 2]
    dp = [[0 for _ in range(elems)] for _ in range(n)]

    for i, e in enumerate(list_of_abc[0]):
        dp[0][i] = e

    for i in range(1, n):
        for todays_act in range(elems):
            for yesterdays_act in range(elems):
                if todays_act == yesterdays_act:
                    continue
                dp[i][todays_act] = max(
                        dp[i][todays_act],
                        dp[i - 1][yesterdays_act] + list_of_abc[i][todays_act]
                )

    return max(dp[n - 1])


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()