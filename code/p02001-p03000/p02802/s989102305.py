import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(2, [[1, 'WA'], [1, 'AC'], [2, 'WA'], [2, 'AC'], [2, 'WA']]),
            (2, 2)
        )

    def test_2(self):
        self.assertEqual(
            think(100000, [[7777, 'AC'], [7777, 'AC'], [7777, 'AC']]),
            (1, 0)
        )

    def test_3(self):
        self.assertEqual(
            think(6, []),
            (0, 0)
        )


def solve():
    n, list_of_p_and_s = read()
    result = think(n, list_of_p_and_s)
    write(result)


def read():
    n, m = read_int(2)
    list_of_p_and_s = []
    for _ in range(m):
        p_and_s = input().split(' ')[:2]
        list_of_p_and_s.append([int(p_and_s[0]), p_and_s[1]])
    return n, list_of_p_and_s


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


def think(n, list_of_p_and_s):
    ac = [False for _ in range(n + 1)]
    penalty = [0 for _ in range(n + 1)]

    for p, s in list_of_p_and_s:
        if s == 'AC':
            ac[p] = True
        elif s == 'WA':
            if ac[p]:
                continue
            else:
                penalty[p] += 1
        else:
            raise RuntimeError()

    count_a = 0
    sum_penalty = 0
    for a, p in zip(ac, penalty):
        if a:
            count_a += 1
            sum_penalty += p
    return count_a, sum_penalty


def write(result):
    print('{0:d} {1:d}'.format(result[0], result[1]))


if __name__ == '__main__':
    # unittest.main()
    solve()