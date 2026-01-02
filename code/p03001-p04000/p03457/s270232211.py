import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())

    t = 0
    x = 0
    y = 0

    ans = True

    for _ in range(n):
        next_t, next_x, next_y = map(int, input().split())

        dist = abs(next_x - x) + abs(next_y - y)

        if next_t - t == dist:
            t, x, y = next_t, next_x, next_y
        elif next_t - t > dist and ((next_t - t) - dist) % 2 == 0:
            t, x, y = next_t, next_x, next_y
        else:
            ans = False
            break

    if ans:
        print('Yes')
    else:
        print('No')




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
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()