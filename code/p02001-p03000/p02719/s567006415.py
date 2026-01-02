import sys
from io import StringIO
import unittest


def resolve():
    n, k = map(int, input().split())

    if n == 0:
        print("0")
        return

    if k == 1:
        print("0")
        return

    # いつ最小になるか = 桁が変わる前後のタイミング。
    q, mod = divmod(n, k)
    # print(q, mod)
    # 7 と　4　の場合：1　あまり 3。

    # 3 から 一回だけ引いてみる。
    minus_edge = abs(mod - k)

    print(str(min(mod, minus_edge)))




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
        input = """7 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1000000000000000000 1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()