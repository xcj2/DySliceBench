import sys
from io import StringIO
import unittest
from collections import Counter

def resolve():
    n = int(input())
    a = sorted(list(map(int, input().split())))

    counter = Counter(a)

    ans = 0

    for key, value in counter.items():
        if key == 0:
            tmp = counter[key + 1] + value
        else:
            tmp = counter[key + 1] + counter[key] + counter[key - 1]

        if ans < tmp:
            ans = tmp

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
        input = """7
3 1 4 1 5 9 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10
0 1 2 3 4 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1
99999"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()