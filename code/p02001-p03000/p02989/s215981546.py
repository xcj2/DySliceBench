import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([9, 1, 4, 4, 6, 7]), 2)

    def test_2(self):
        self.assertEqual(think([9, 1, 14, 5, 5, 4, 4, 14]), 0)

    def test_3(self):
        self.assertEqual(think([99592 ,10342 ,29105 ,78532 ,83018 ,11639 ,92015 ,77204 ,30914 ,21912 ,34519 ,80835 ,100000 ,1]), 42685)


def solve():
    d = read()
    result = think(d)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(data):
    n = len(data)
    data.sort()
    right_index = n // 2
    left_index = n // 2 - 1
    return data[right_index] - data[left_index]


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()