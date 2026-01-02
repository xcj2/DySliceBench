import sys
from io import StringIO
import unittest
import math


def resolve():
    N = int(input())
    A = 1
    B = 1

    center = math.ceil(math.sqrt(N))
    for i in range(1, center + 1)[::-1]:
        if N % i == 0:
            A = i
            B = int(N / i)
            break
        else:
            continue

    result = A - 1 + B - 1
    print(result)


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
