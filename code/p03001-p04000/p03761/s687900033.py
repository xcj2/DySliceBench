import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    ss = [input() for _ in range(n)]

    alphabets = [chr(ord('a') + x) for x in range(26)]

    ans = [0 for _ in range(26)]
    for i, a in enumerate(alphabets):
        ans[i] = min([s.count(a) for s in ss])

    ans_str = ''

    for a, cnt in zip(alphabets, ans):
        ans_str += a * cnt

    print(ans_str)

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
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main(
    resolve()
