import unittest


class TestE(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
                think(2, [1, 1, 3, 4]),
                11
        )

    def test_2(self):
        self.assertEqual(
                think(3, [10, 10, 10, -10, -10, -10]),
                360
        )

    def test_3(self):
        self.assertEqual(
                think(1, [1, 1, 1]),
                0
        )

    def test_4(self):
        self.assertEqual(
                think(6, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0, 0, 0, 0, 0]),
                999998537
        )


def solve():
    k, a = read()
    result = think(k, a)
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


def think(k, a):
    mode = 10 ** 9 + 7
    n = len(a)

    fact_table, inverse_fact_table = prepare_fact_table(n, mode)
    a.sort()

    sum_of_max = 0
    sum_of_min = 0

    for i, x in enumerate(a):
        if i >= k - 1:
            sum_of_max += x * combination(i, k - 1, fact_table, inverse_fact_table, mode)
            sum_of_max %= mode
        if n - i >= k:
            sum_of_min += x * combination(n - i - 1, k - 1, fact_table, inverse_fact_table, mode)
            sum_of_min %= mode

    return (sum_of_max - sum_of_min) % mode


def write(result):
    print(result)


def prepare_fact_table(n, mode):
    fact_table = [1 for i in range(n + 1)]
    inverse_fact_table = [1 for i in range(n + 1)]
    for i in range(2, len(fact_table)):
        fact_table[i] = fact_table[i - 1] * i % mode
        inverse_fact_table[i] = divmod(fact_table[i], mode)
    return fact_table, inverse_fact_table


def divmod(x, mode):
    return pow(x, mode - 2, mode)


def combination(n, k, fact_table, inverse_fact_table, mode):
    return fact_table[n] * inverse_fact_table[k] * inverse_fact_table[n - k] % mode


if __name__ == '__main__':
    # unittest.main()
    solve()