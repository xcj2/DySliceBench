import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4, 9, 2, 3), 2)

    def test_2(self):
        self.assertEqual(think(10, 40, 6, 8), 23)

    def test_3(self):
        self.assertEqual(think(314159265358979323, 846264338327950288, 419716939, 937510582), 532105071133627368)

    def test_4(self):
        self.assertEqual(count_multiple_between(4, 9, 2), 3)

    def test_5(self):
        self.assertEqual(count_multiple_between(4, 9, 3), 2)

    def test_6(self):
        self.assertEqual(count_multiple_between(4, 9, 6), 1)

    def test_7(self):
        self.assertEqual(count_multiple_between(10, 40, 6), 5)

    def test_8(self):
        self.assertEqual(count_multiple_between(10, 40, 8), 4)

    def test_9(self):
        self.assertEqual(count_multiple_between(10, 40, 24), 1)


def solve():
    a, b, c, d = read()
    result = think(a, b, c, d)
    write(result)


def read():
    return read_int(4)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b, c, d):
    if c > d:
        return think(a, b, d, c)

    if c == 1:
        return 0

    if d % c == 0:
        num_of_multiple = count_multiple_between(a, b, c)
        return b - a + 1 - num_of_multiple

    lcm = least_common_multiple(c, d)

    num_of_multiple_c = count_multiple_between(a, b, c)
    num_of_multiple_d = count_multiple_between(a, b, d)
    num_of_multiple_lcm = count_multiple_between(a, b, lcm)

    return b - a + 1 - (num_of_multiple_c + num_of_multiple_d - num_of_multiple_lcm)


def count_multiple_between(a, b, c):
    minimum_multiple = a if a % c == 0 else a + (c - (a % c))
    maximum_mulptile = b if b % c == 0 else b - (b % c)

    if maximum_mulptile < minimum_multiple:
        return 0

    return (maximum_mulptile - minimum_multiple) // c + 1


def least_common_multiple(a, b):
    return (a * b) // greatest_common_divisor(a, b)


def greatest_common_divisor(a, b):
    if a < b:
        return greatest_common_divisor(b, a)

    if a % b == 0:
        return b
    return greatest_common_divisor(b, a % b)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()