import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    v = list(map(int, input().split()))

    v.sort()

    ans = (v[0] + v[1]) / 2

    for i in range(2, len(v)):
        ans = (ans + v[i]) / 2

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
        input = """2
3 4"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
500 300 200"""
        output = """375"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
138 138 138 138 138"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
