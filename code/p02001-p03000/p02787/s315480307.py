import sys
from io import StringIO
import unittest
import math
from collections import deque


def resolve():
    hp, n = map(int, input().split())
    magics = [list(map(int, input().split())) for i in range(n)]

    max_magic_power = 0
    # min_magic_power = 99999

    for magic in magics:
        max_magic_power = max(max_magic_power, magic[0])
        # min_magic_power = min(min_magic_power, magic[0])

    # dp作成[与えることができる最大ダメージ]×2(配列再利用と呼ばれる DP 時のメモリ消費を抑えるテクニックを使うので、2つで十分)
    # dp = [[0 for i in range(hp + max_magic_power)] for j in range(2)]

    # 想定できる最大魔法実施回数(HP / 一番弱い魔法)
    # max_cnt = math.ceil(hp / min_magic_power)

    # for cnt, i in enumerate(range(max_cnt)):
    #     now = cnt % 2
    #     bef = (cnt + 1) % 2
    #
    #     for magic in magics:
    #         dp[now][]

    # ダメージ量ごとに処理を行うため、キューを作成
    que = deque()

    ans = [999999999 for i in range(hp + max_magic_power + 1)]
    ans[0] = 0

    # # 初期データを格納(ダメージ0,消費MP0)
    # que.append([0, 0])
    #
    # while len(que) is not 0:
    #     damage, use_mp = que.pop()
    #
    #     # HP以上のダメージを与え終えた場合、何もせず終了
    #     if damage >= hp:
    #         continue
    #
    #     for magic in magics:
    #         # 各魔法を使用した結果をシュミレーション
    #         work_damage = damage + magic[0]
    #         work_use_mp = use_mp + magic[1]
    #
    #         # 消費MPが少ないパターンを発見できた場合
    #         if ans[work_damage] > work_use_mp:
    #             # 結果を更新
    #             ans[work_damage] = work_use_mp
    #             # キューに追加(継続して検証する)
    #             que.append([work_damage, work_use_mp])
    #
    # print(min(ans[hp-1:hp + 10000]))

    # HPの数だけループすればOK(残りHP1で魔法の威力10・・とかも、これで検証できるので。
    for i in range(hp + 1):
        # 与えることができないパターンのダメージなら、何もしない。
        if ans[i] is 999999999:
            continue

        # 与えることができるパターンのダメージなら、さらに、全魔法を打ち込んだ場合を検証。
        for magic in magics:
            # ans[合計ダメージ量] = min(ans[合計ダメージ量] , ans[蓄積ダメージ量] + 今回の魔法の消費HP
            # ※ans[]は、各ダメージ量の場合の、最小消費MPを保持する。
            ans[i + magic[0]] = min(ans[i + magic[0]], ans[i] + magic[1])

    print(min(ans[hp:-1]))


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
        input = """9 3
8 3
4 2
2 1"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100 6
1 1
2 3
3 9
4 27
5 81
6 243"""
        output = """100"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461"""
        output = """139815"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """10000 1
1 10000
"""
        output = """100000000"""
        self.assertIO(input, output)



if __name__ == "__main__":
    # unittest.main()
    resolve()