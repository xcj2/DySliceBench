import sys
from io import StringIO
import unittest


def resolve():
    # s = input()
    # n = int(input())
    x, y = map(int, input().split())
    # l = [list(map(int, input().split())) for _ in range(n)]

    if y <= 4 * x and 2 * x <= y and y % 2 == 0:
        print('Yes')
    else:
        print('No')

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
        input = """3 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
