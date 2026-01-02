import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('3776'), 'Bad')

    def test_2(self):
        self.assertEqual(think('8080'), 'Good')

    def test_3(self):
        self.assertEqual(think('1333'), 'Bad')

    def test_4(self):
        self.assertEqual(think('0024'), 'Bad')


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    length_of_string = 4
    return read_line(n=length_of_string)


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
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            return 'Bad'
    return 'Good'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()