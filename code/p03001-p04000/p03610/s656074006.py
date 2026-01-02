#
# abc072 b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    s = input()

    ans = ""
    for i in range(len(s)):
        if (i+1) % 2 == 1:
            ans += s[i]
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
        input = """atcoder"""
        output = """acdr"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaaa"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """z"""
        output = """z"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """fukuokayamaguchi"""
        output = """fkoaaauh"""
        self.assertIO(input, output)


if __name__ == "__main__":
    #unittest.main()
    resolve()
