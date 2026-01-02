#
# abc082 b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    s = list(input())
    t = list(input())

    flag = False
    s = sorted(s)
    t = sorted(t, reverse=True)

    if s < t:
        print("Yes")
    else:
        print("No")


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
        input = """yx
axy"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ratcode
atlas"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """cd
abc"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """w
ww"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """zzz
zzz"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
