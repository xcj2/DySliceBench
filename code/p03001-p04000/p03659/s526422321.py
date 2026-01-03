import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    ans = []
    x = 0
    for i in range(n - 1):
        x += a[i]
        y = total - x

        ans.append(abs(x - y))

    print(min(ans))


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
        input = """6
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
10 -10"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()