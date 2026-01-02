import sys
from io import StringIO
import unittest
from collections import deque

def resolve():
    n, k = map(int, input().split())

    a_s = list(map(int, input().split()))
    # 添え字は0始まり、町番号は1始まりなので、添え字0を足し込んで値を合わせる
    a_s.insert(0, 0)

    # 到達済みフラグ(添え字0は使わないので+1
    # arrived = [False for i in range[n+1]]

    # 町1からの距離(添え字0は使わないので+1
    distance = [-1 for i in range(n+1)]
    # 初期値：町1は町1との距離0
    distance[1] = 0

    # queを作成
    que = deque()
    que.append(1) # 初期値：町1

    # 答えを求めるために必要な情報を種痘
    while len(que) is not 0:

        now = que.pop()
        next = a_s[now]
        if distance[next] is not -1:
            # 循環が発生
            # 町1からループが発生する町までの距離
            # 例：1->6->2->5->3->2->5->2->5->3 ・・・というパターンの場合は「2」。2->5->3->2がループなので。
            no_loop = distance[next]
            # ループが発生する町(ループ始点)からループが発生する町(ループ終点)までの距離
            loop = distance[now] - distance[next]

        else:
            # 新しい街に到達した場合
            # 町1からの距離を設定
            distance[next] = distance[now] + 1
            # 次のとび先をキューに追加
            que.append(next)

    # 答えを出力(方程式の信頼性はトレース.xlsxを見ると良い。多分問題ない・・!
    if k <= no_loop:
        print(distance.index(k))
    else:
        print(distance.index((k - no_loop) % (loop + 1) + no_loop))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
#     def test_入力例_1(self):
#         input = """4 5
# 3 2 4 1"""
#         output = """4"""
#         self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()