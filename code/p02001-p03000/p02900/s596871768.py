import sys
from io import StringIO
import unittest


def factorization(n):
    if n == 1:
        return {}
    d = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            d[i] = cnt

    if temp != 1:
        d[temp] = 1

    if d == {}:
        d[n] = 1

    return d


def resolve():
    A, B = map(int, input().split())
    A_f = factorization(A)
    B_f = factorization(B)

    d = {}
    for key_A, value_A in A_f.items():
        if key_A not in B_f:
            continue
        d[key_A] = max(value_A, B_f[key_A])

    print(len(d.keys()) + 1)


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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
