import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(2, 10, 20),
            [30, 50, 90, 170, 330, 650, 1290, 2570, 5130, 10250]
        )

    def test_2(self):
        self.assertEqual(
            think(4, 40, 60),
            [200, 760, 3000, 11960, 47800, 191160, 764600, 3058360, 12233400, 48933560]
        )


def solve():
    r, d, x = read()
    result = think(r, d, x)
    write(result)


def read():
    return read_int(3)


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


def think(r, d, x):
    length = 10
    result = [x]
    for i in range(length):
        result.append(result[-1] * r - d)
    return result[1:]


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    # unittest.main()
    solve()