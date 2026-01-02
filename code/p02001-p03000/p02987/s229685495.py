import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('ASSA'), 'Yes')

    def test_2(self):
        self.assertEqual(think('STOP'), 'No')

    def test_3(self):
        self.assertEqual(think('FFEE'), 'Yes')

    def test_4(self):
        self.assertEqual(think('FREE'), 'No')


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


def think(s):
    for i in range(len(s)):
        if s.count(s[i]) == 2:
            continue
        else:
            return 'No'
    return 'Yes'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()