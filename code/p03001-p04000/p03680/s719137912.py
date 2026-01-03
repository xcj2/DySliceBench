import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    ans = 0
    next_i = 1
    goal = False
    for _ in range(n):
        next_i = a[next_i - 1]
        ans += 1
        if next_i == 2:
            goal = True
            break

    if goal:
        print(ans)
    else:
        print(-1)


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
3
1
2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()