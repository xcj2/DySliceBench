import sys
from io import StringIO
import unittest


def num_divisors_table(n):
    table = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1

    return table

def resolve():
    n = int(input())

    ans = num_divisors_table(n)

    print(sum([i * a for i, a in enumerate(ans)]))



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
        input = """4"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """26879"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """838627288460105"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
