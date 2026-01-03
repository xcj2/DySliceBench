#
# abc065 a
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    r, b, g = map(int, input().split())
    if (100*r+10*b+g) % 4 == 0:
        print("YES")
    else:
        print("NO")


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
        input = """4 3 2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 4"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
