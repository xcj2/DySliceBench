import sys
from io import StringIO
import unittest

import math

def resolve():
    n, m = map(int, input().split())
    div = 10**9 + 7

    # n! * m! * 2
    if abs(n - m) > 1:
        print(0)
    elif n == m:
        print((math.factorial(n) * math.factorial(m) * 2) % div)
    else:
        print((math.factorial(n) * math.factorial(m)) % div)

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
        input = """2 2"""
        output = """8"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 2"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """100000 100000"""
        output = """530123477"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()