#
# abc085 a
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    S = input()
    print(S[0:3]+"8"+S[4:])


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
        input = """2017/01/07"""
        output = """2018/01/07"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2017/01/31"""
        output = """2018/01/31"""
        self.assertIO(input, output)


if __name__ == "__main__":
    #unittest.main()
    resolve()
