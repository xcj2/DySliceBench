import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    s = list(input())

    ans = 0
    for i in range(len(s) - 1):
        left = s[0:i + 1]
        right = s[i + 1:]

        tmp_ans = len(set(left) & set(right))

        # if ans < tmp_ans:
        #     ans = tmp_ans
        ans = max(ans, tmp_ans)

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
        input = """6
aabbca"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()