import sys
from io import StringIO
import unittest

def resolve():
    N, = map(int, input().split())
    As = list(map(int, input().split()))
    ans = 0
    last = 0
    for a in As:
        dif = max(0,last-a)
        last = a+dif
        ans = ans+dif


    print("{}".format(ans))

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
        input = """5
2 1 5 4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 3 3 3 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
