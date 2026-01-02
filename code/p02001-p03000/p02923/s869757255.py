import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    hh = list(map(int, input().split()))

    ans = 0
    tmp_ans = 0
    h = hh[0]
    for next_h in hh[1:]:
        if h >= next_h:
            tmp_ans += 1
        else:
            if ans < tmp_ans:
                ans = tmp_ans
            tmp_ans = 0

        h = next_h

    if ans < tmp_ans:
        ans = tmp_ans

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
        input = """5
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()