#
# abc144 c
#
import unittest
from io import StringIO
import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    N = int(input())

    S = math.ceil(math.sqrt(N))
    ans = N - 1

    for i in range(1, S+1):
        if N % i == 0:
            j = N // i
            ans = min(ans, i+j-2)
    print(ans)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[: -1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """50"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000019"""
        output = """10000000018"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
