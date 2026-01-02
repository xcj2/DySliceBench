import sys
from io import StringIO
import unittest
import itertools

# タグ、順列、組み合わせ

# abcd・・a=<b=<=<d・・という塊は、広義単調増加等と言うらしい。
#     参考：単調増加等の説明：https://mathtrain.jp/tantyou
# そして、この組み合わせを網羅するには、重複組合せを使える。
#     参考：重複組合せ：https://mathtrain.jp/tyohukuc
# 最大の組み合わせ数は20C10になる、と思ったが、違う。20C10が正しいらしい。
# 実装方法はこんな感じ。
#     https://qiita.com/junkls/items/10384950963056cc8e08
# 問題文の意味が分かりずらい・・15分かかった。
# 例)
# ---入力例---
#   3 4 3
#   1 3 3 100
#   1 2 2 10
#   2 3 2 10

#   1 3 3 100の場合・・
#   「3番目の数字 - 1番目の数字 = 3になる場合100点加算。」という意味。

# ---出力---
#   110
#   ->A[1, 3, 4]の時・・
#     「1 3 3 100」->A[3](つまり4) - A[1](つまり1) = 3 だから100点加算。
#     「1 2 2  10」->A[2](つまり3) - A[1](つまり1) = 2 だから 10点加算。
#     「2 3 2  10」->A[3](つまり4) - A[2](つまり3) = 1(=2じゃない) だから 加算なし。

def resolve():
    n, m, q = map(int, input().split())

    num_list = [list(map(int, input().split())) for i in range(q)]

    targets = list(itertools.combinations_with_replacement(range(1, m+1), n))

    point = 0
    for target in targets:
        work_point = 0
        for num in num_list:
            # 条件を満たすならポイント加算。
            # ※targetsは0始まりの配列、num_listは1始まるの値が格納されているので、targetの添え字を指定するとき-1している。
            if target[num[1]-1] - target[num[0]-1] == num[2]:
                work_point += num[3]

        # 最適解を格納
        point = max(point, work_point)

    print(point)




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
        input = """3 4 3
1 3 3 100
1 2 2 10
2 3 2 10"""
        output = """110"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328"""
        output = """357500"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()