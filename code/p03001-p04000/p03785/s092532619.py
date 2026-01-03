import sys
from io import StringIO
import unittest

def resolve():
    n, c, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]

    t.sort()
    ans = 1
    bus_base = t[0] + k
    cnt_bus = 0

    for i in range(n):
        if cnt_bus == c:
            cnt_bus = 0
            bus_base = t[i] + k
            ans += 1

        if t[i] <= bus_base:
            cnt_bus += 1
            continue
        else:
            bus_base = t[i] + k
            ans += 1
            cnt_bus = 1

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
        input = """5 3 5
1
2
3
6
12"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 3 3
7
6
2
8
10
6"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()