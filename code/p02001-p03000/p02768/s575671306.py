import sys
from io import StringIO
import unittest
from math import factorial

div = 10 ** 9 + 7

def cnt_combination(n, r):
    res = 1
    fac = 1

    for i in range(r):
        res *= n - i
        res %= div
        fac *= i + 1
        fac %= div

    return res * pow(fac, div - 2, div) % div


def resolve():
    n, a, b = map(int, input().split())
    ans = pow(2, n, div) - 1
    print((ans - cnt_combination(n, a) - cnt_combination(n, b)) % div)

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
        input = """4 1 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1000000000 141421 173205"""
        output = """34076506"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()