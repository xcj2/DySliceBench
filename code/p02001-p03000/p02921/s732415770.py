import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    t = input()
    ans = 0
    for i, j in zip(s, t):
        if i == j:
            ans += 1
    print(ans)


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
        input = """CSS
CSR"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """SSR
SSR"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """RRR
SSS"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
