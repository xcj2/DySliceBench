import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    x = list(map(int, input().split()))
    p1 = int(sum(x)/n)
    p2 = p1 + 1

    ans1 = [(x_-p1)**2 for x_ in x]
    ans2 = [(x_-p2)**2 for x_ in x]

    print(min(sum(ans1), sum(ans2)))
    


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
        input = """2
1 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
14 14 2 13 56 2 37"""
        output = """2354"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
