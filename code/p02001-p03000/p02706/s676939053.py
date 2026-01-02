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
        input = """41 2
5 6"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
5 6"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 2
5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """314 15
9 26 5 35 8 9 79 3 23 8 46 2 6 43 3"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    n, a = read()
    result = think(n, a)
    write(result)


def read():
    n, m = read_int(2)
    return n, read_int(m)


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


def think(n, a):
    total = sum(a)
    return -1 if n < total else n - total


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    resolve()