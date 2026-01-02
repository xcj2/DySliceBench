import sys
from io import StringIO
import unittest


def resolve():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))

    if p == [] or x not in p:
        print(x)
    else:
        p = set(p)
        i = 1
        while 1:
            if x - i not in p:
                print(x - i)
                break
            elif x + i not in p:
                print(x + i)
                break
            else:
                i += 1



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
        input = """6 5
4 7 10 6 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 5
4 7 10 6 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 0"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
