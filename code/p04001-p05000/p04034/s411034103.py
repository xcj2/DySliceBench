import sys
from io import StringIO
import unittest

def resolve():
    n, m = map(int, input().split())

    red = [0 for _ in range(n)]
    red[0] = 1
    balls = [1 for _ in range(n)]

    for _ in range(m):
        x, y = map(int, input().split())

        if red[x - 1] == 1:
            red[y - 1] = 1

        balls[x - 1] -= 1
        balls[y - 1] += 1

        if balls[x - 1] == 0:
            red[x - 1] = 0

    print(sum(red))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """3 2
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()