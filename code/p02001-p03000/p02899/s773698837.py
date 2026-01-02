import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([2, 3, 1]), [3, 1, 2])

    def test_2(self):
        self.assertEqual(think([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_3(self):
        self.assertEqual(think([8, 2, 7, 3, 4, 5, 6, 1]), [8, 2, 4, 5, 6, 7, 3, 1])


def solve():
    a = read()
    result = think(a)
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


def think(a):
    list_of_index_and_a = []
    for index, e in enumerate(a):
        list_of_index_and_a.append((index + 1, e))

    list_of_index_and_a.sort(key=lambda x: x[1])
    return [x[0] for x in list_of_index_and_a]


def write(result):
    print(' '.join(list(map(lambda x: str(x), result))))


if __name__ == '__main__':
    # unittest.main()
    solve()