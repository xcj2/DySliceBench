import sys
from io import StringIO
import unittest


def resolve():
    s = list(input())
    ll = len(s)
    ans = 0

    if ll % 2 == 0:
        for i in range(0, ll, 2):
            if i == 0:
                if s[:ll//2+1] == s[ll//2 + 1:]:
                    ans = ll//2
                    break
            else:
                tmp = s[:(-1 * i)]
                if tmp[:len(tmp)//2] == tmp[len(tmp)//2:]:
                    ans = len(tmp)
                    break
    else:
        for i in range(1, ll, 2):
            tmp = s[:-i]
            if tmp[:len(tmp)//2] == tmp[len(tmp)//2:]:
                ans = len(tmp)//2
                break
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
        input = """abaababaab"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """xxxx"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """abcabcabcabc"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """akasakaakasakasakaakas"""
        output = """14"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()