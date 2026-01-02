import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    A, B = map(int, input().split())
    ans = A-2*B
    if ans > 0:
        print(ans)
    else:
        print("0")


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
        input = """12 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 15"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 30"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
