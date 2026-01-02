import sys
from io import StringIO
import unittest


# https://atcoder.jp/contests/abc083/tasks/arc088_a
# 入力例1、間違ってね?
# 入力；3 20 で、出力3。これは分かるが・・「数式3,6,18」が条件を満たします。->「3,6,12」じゃね?
# その前提でやってみよう。

def resolve():
    # ★get input
    x, y = map(int, input().split())

    count = 0
    work_x = x
    while work_x <= y:
        count += 1
        work_x = work_x*2

    print(count)



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
        input = """3 20"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """25 100"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """314159265 358979323846264338"""
        output = """31"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()