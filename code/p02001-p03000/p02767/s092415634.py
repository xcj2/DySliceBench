import sys
from io import StringIO
import unittest
from decimal import Decimal, ROUND_HALF_UP


def resolve():
    N = int(input())
    X = [int(i) for i in input().split()]
    p = int(Decimal(str(sum(X) / N))
            .quantize(Decimal("0"), rounding=ROUND_HALF_UP))
    sumXP = 0
    for xi in X:
        sumXP += (xi - p)**2
    print(sumXP)


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
