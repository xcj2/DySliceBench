import sys
from io import StringIO
import unittest


def resolve():
    N, K = map(int, input().split())
    S = list(input())
    S[K - 1] = S[K - 1].lower()
    print(''.join(S))


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
        input = """3 1
ABC"""
        output = """aBC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
CABA"""
        output = """CAbA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
