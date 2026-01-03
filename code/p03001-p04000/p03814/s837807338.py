#
# abc053 b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    s = input()

    S = 0
    E = len(s)
    for i in range(len(s)):
        if s[i] == "A":
            S = i
            break
    for j in reversed(range(len(s))):
        if s[j] == "Z":
            E = j+1
            break
    print(len(s[S:E]))


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
        input = """QWERTYASDFZXCV"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ZABCZ"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """HASFJGHOGAKZZFEGA"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
