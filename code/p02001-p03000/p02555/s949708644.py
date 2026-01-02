import sys
from io import StringIO
import unittest
MOD = 1000000007
def resolve():
    S, = map(int, input().split())
    n = [0]*(S+1)
    n[0]=1
    for i in range(S+1):
        for j in range(3,i+1):
            left = i-j
            n[i]=(n[i]+n[left])%MOD


    print(n[S])
class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(output, out)

    def test_入力例_1(self):
        input = """7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1729"""
        output = """294867501"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
