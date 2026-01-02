#
# abc095 b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    N, X = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = int(input())

    R = X - sum(m)
    ans = N + R // min(m)
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
        input = """3 1000
120
100
140"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 360
90
90
90
90"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 3000
150
130
150
130
110"""
        output = """26"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
	resolve()