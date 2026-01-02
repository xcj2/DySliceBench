import sys
from io import StringIO
import unittest

def resolve():
    N = map(int, input().split())
    input_str = input()
    r_cnt=0;
    for s in input_str:
        # print(s)
        if s =='R':
            r_cnt+=1
    ans = 0
    for i in range(r_cnt):
        if input_str[i] == 'W':
            ans+=1
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
        input = """4
WWRR"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
RR"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
WRWWRWRR"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
