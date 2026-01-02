import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('SAT'), 1)

    def test_2(self):
        self.assertEqual(think('SUN'), 7)


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    return read_line()


def read_int(n):
    return read_type(int, n)


def read_float(n):
    return read_type(float, n)


def read_type(t, n):
    return list(map(lambda x: t(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(data):
    weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return len(weekday) - weekday.index(data)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()