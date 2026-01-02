import sys
from io import StringIO
import unittest


def resolve():
    # s = input()
    n = int(input())
    a = [int(input()) for _ in range(n)]
    # l = [list(map(int, input().split())) for _ in range(n)]
    aa = sorted(a)

    max_1st = aa[-1]
    max_2nd = aa[-2]

    for i, a_i in enumerate(a):
        if max_1st == a_i:
            print(max_2nd)
        else:
            print(max_1st)


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
        input = """3
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
