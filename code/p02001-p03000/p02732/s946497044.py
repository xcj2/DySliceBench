import sys
from io import StringIO
import unittest

def resolve():

    n = int(input())
    a_s = list(map(int, input().split()))

    numdict = {}
    for a in a_s:
        numdict[a] = numdict.get(a, 0) + 1

    # bannしない場合のパターン数を得る。
    all_cnt = 0
    for val in numdict.values():
        all_cnt += val*(val-1) / 2

    # k番目を除いた場合のパターン数を出力していく。
    for a in a_s:
        # k番目が存在しない場合の影響数を取得
        val = numdict[a]
        work = (val-1)*(val-1-1) / 2 - val*(val-1) / 2
        print(int(all_cnt + work))



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
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()




