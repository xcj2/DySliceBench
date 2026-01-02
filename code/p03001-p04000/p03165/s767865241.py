import unittest


class TestF(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            len(think('axyb', 'abyxb')),
            3
        )

    def test_2(self):
        self.assertEqual(
            len(think('aa', 'xayaz')),
            2
        )

    def test_3(self):
        self.assertEqual(
            len(think('a', 'z')),
            0
        )

    def test_4(self):
        self.assertEqual(
            len(think('abracadabra', 'avadakedavra')),
            7
        )


def solve():
    s, t = read()
    result = think(s, t)
    write(result)


def read():
    s = read_line()
    t = read_line()
    return s, t


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


def think(s, t):
    # dp[0][j] = 0
    # dp[i][j] = 0
    # dp[i + 1][j + 1] = max len of LCS for s[0 to ith] and t[0 to jth]
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    for i in range(len(s)):
        if s[i] == t[0]:
            dp[i + 1][1] = 1
        if i > 0 and dp[i][1] == 1:
            dp[i + 1][1] = 1
    for j in range(len(t)):
        if t[j] == s[0]:
            dp[1][j + 1] = 1
        if j > 0 and dp[1][j] == 1:
            dp[1][j + 1] = 1

    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(
                    dp[i + 1][j],
                    dp[i][j + 1]
                )

    return restore_lcs(s, t, dp)


def write(result):
    print(result)


def restore_lcs(s, t, dp):
    lcs = ''
    i, j = len(s), len(t)

    while i >= 0 and j >= 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
            continue
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
            continue
        lcs += s[i - 1]
        i -= 1
        j -= 1

    return lcs[::-1]


if __name__ == '__main__':
    # unittest.main()
    solve()