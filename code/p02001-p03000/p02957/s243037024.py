import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 16), '9')

    def test_2(self):
        self.assertEqual(think(0, 3), 'IMPOSSIBLE')

    def test_3(self):
        self.assertEqual(think(998244353, 99824435), '549034394')


def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    return read_int(2)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b):
    if abs(a - b) % 2 == 0:
        return str(min(a, b) + abs(a - b) // 2)
    return 'IMPOSSIBLE'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()