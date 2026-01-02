import sys
from io import StringIO
import unittest
import copy

def resolve():
    n, m, x = map(int, input().split())

    books = [list(map(int, input().split())) for i in range(n)]

    ans = 99999999

    # bit全探索
    # 本の数だけパターンを作成
    for i in range(1 << n):

        price = 0
        rikais = [0 for i in range(m)]

        # 本の数だけループ
        for j in range(n):

            # 値が1(購入)の場合
            if i & 1 << j:
                # 価格を加算
                price += books[j][0]
                # 理解度を加算
                for k in range(1, m+1):
                    rikais[k-1] += books[j][k]

            # すべてのアルゴリズムの理解度をX以上にできた場合
            if min(rikais) >= x:
                # 価格の最適解を更新
                ans = min(price, ans)

    # 価格を出力
    if ans is 99999999:
        print(-1)
    else:
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
        input = """3 3 10
60 2 2 4
70 8 7 9
50 2 3 9"""
        output = """120"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 3 10
100 3 1 4
100 1 5 9
100 2 6 5"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2"""
        output = """1067"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()