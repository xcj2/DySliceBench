import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think([1, 1, 2, 1, 2]),
            [2, 2, 3, 2, 3]
        )

    def test_2(self):
        self.assertEqual(
            think([1, 2, 3, 4]),
            [0, 0, 0, 0]
        )

    def test_3(self):
        self.assertEqual(
            think([3, 3, 3, 3, 3]),
            [6, 6, 6, 6, 6]
        )

    def test_4(self):
        self.assertEqual(
            think([1, 2, 1, 4, 2, 1, 4, 1]),
            [5, 7, 5, 7, 7, 5, 7, 5]
        )


def solve():
    a = read()
    result = think(a)
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


def think(a):
    hist = make_hist(a)
    num_of_pair = calc_num_of_pair(hist)
    sum_of_num_of_pair = 0

    result = [0] * len(a)

    for k, v in num_of_pair.items():
        sum_of_num_of_pair += v

    for i, e in enumerate(a):
        if hist[e] <= 1:
            result[i] = sum_of_num_of_pair
        else:
            n = hist[e]
            result[i] = sum_of_num_of_pair - num_of_pair[e]
            result[i] += ((n - 1) * (n - 2)) // 2
    return result


def make_hist(a):
    hist = {}
    for e in a:
        hist[e] = hist.get(e, 0) + 1
    return hist


def calc_num_of_pair(hist):
    num_of_pair = {}
    for k, v in hist.items():
        if v <= 1:
            num_of_pair[k] = 0
        else:
            num_of_pair[k] = (v * (v - 1)) // 2
    return num_of_pair


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    # unittest.main()
    solve()