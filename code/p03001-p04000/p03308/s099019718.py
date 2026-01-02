#
# abc102 b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    print(A[-1]-A[0])


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
        input = """4
1 4 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1000000000 1"""
        output = """999999999"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
