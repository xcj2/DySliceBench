import sys
from io import StringIO
import unittest

def resolve():
    N, = map(int, input().split())

    kmin=100000000000
    kmax = 0
    lmin = 100000000000
    lmax = 0
    for i in range(N):
        x,y = map(int, input().split())
        k = y-x
        l = y+x
        kmin = min(kmin,k)
        lmin = min(lmin, l)
        kmax = max(kmax, k)
        lmax = max(lmax, l)


    print(max(kmax-kmin,lmax-lmin))
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
        input = """3
1 1
2 4
3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
