#
# abc144 a
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    A, B = map(int, input().split())

    if 1 <= A <= 9 and 1 <= B <= 9:
        print(A*B)
    else:
        print("-1")


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
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 10"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 9"""
        output = """81"""
        self.assertIO(input, output)


if __name__ == "__main__":
    #unittest.main()
    resolve()
