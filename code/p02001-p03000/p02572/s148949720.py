import sys
from io import StringIO
import unittest

modn=1000000007

def resolve():
    n = input()
    inputs = list(map(int, input().split()))
    sum_value = sum(inputs)% modn
    ans=0
    for i in range(len(inputs)-1):
        v = inputs[i]
        sum_value = sum_value - v
        add_value = (v * sum_value) % modn
        ans+=add_value
        ans = ans%modn
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
        input = """3
1 2 3"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
141421356 17320508 22360679 244949"""
        output = """437235829"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
