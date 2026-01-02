import sys
from io import StringIO
import unittest
import copy

# 検索用タグ、バージョンによる相違点(pypy)

def resolve():
    x, y, a, b, c = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))

    p.sort(key=lambda xx: -xx)
    q.sort(key=lambda xx: -xx)
    r.sort(key=lambda xx: -xx)

    # 着色を一切行わない場合の値
    # pypy3(2.4.0)ではlist.copy()が未実装。copy をインポートする必要がある。
    def_red = copy.copy(p[0:x])
    def_grren = copy.copy(q[0:y])

    # 無職のリンゴに置換していく・・
    redcnt = -1
    grncnt = -1
    def_red_cnt = len(def_red)
    def_grren_cnt = len(def_grren)

    for i in range(len(r)):
        if not (r[i] > def_red[redcnt] or r[i] > def_grren[grncnt]):
            continue

        if def_red[redcnt] > def_grren[grncnt] and r[i] > def_grren[grncnt]:
            # 透明のリンゴを緑に着色して、置き換える。
            def_grren[grncnt] = r[i]

            if grncnt is not -def_grren_cnt:
                grncnt -= 1

        else:
            # 透明のリンゴを赤に着色して、置き換える。
            def_red[redcnt] = r[i]

            if redcnt is not -def_red_cnt:
                redcnt -= 1


    print(sum(def_red) + sum(def_grren))


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
        input = """1 2 2 2 1
2 4
5 1
3"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 2 2 2 2
8 6
9 1
2 1"""
        output = """25"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 2 4 4 4
11 12 13 14
21 22 23 24
1 2 3 4"""
        output = """74"""
        self.assertIO(input, output)
#     def test_自作成_1(self):
#         input = """1 1 1 1 1
# 10
# 20
# 90"""
#         output = """110"""
#         self.assertIO(input, output)
    # このパターンで「list index out of range」が発生。
#     def test_自作成_2(self):
#         input = """1 1 1 1 2
# 10
# 20
# 90 110"""
#         output = """200"""
#         self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()