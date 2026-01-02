import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """5
1 1 2 2"""
        output = """2
2
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 1 1 1 1 1 1 1 1"""
        output = """9
0
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6"""
        output = """1
1
1
1
1
1
0"""
        self.assertIO(input, output)


def resolve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n - 1)


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
    n = len(a) + 1
    boss = [0] * (n + 1)
    for b in a:
        boss[b] += 1
    return boss[1:]


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    # unittest.main()
    resolve()