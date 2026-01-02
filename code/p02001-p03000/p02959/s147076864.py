import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))

    ans = 0
    for i, b in enumerate(bb):
        a = aa[i]
        next_a = aa[i+1]

        if a < b:
            ans += a
            remain = b - a

            if remain <= next_a:
                ans += remain
                aa[i+1] -= remain
            else:
                ans += next_a
                aa[i+1] = 0
        elif a >= b:
            ans += b

    print(ans)


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
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()