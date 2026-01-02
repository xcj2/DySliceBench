import sys
from io import StringIO
import unittest


def calc(h):
    if h == 1:
        return 1
    else:
        return 2 * calc(h//2) + 1

def resolve():
    h = int(input())
    print(calc(h))


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
        input = """2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000"""
        output = """1099511627775"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
