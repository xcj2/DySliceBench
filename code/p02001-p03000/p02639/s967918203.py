import sys
from io import StringIO
import unittest


def resolve():
    # s = input()
    # n = int(input())
    # a, b = map(int, input().split())
    l = list(map(int, input().split()))

    for i in range(len(l)):
        if l[i] == 0:
            print(i + 1)


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
        input = """0 2 3 4 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 0 4 5"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
