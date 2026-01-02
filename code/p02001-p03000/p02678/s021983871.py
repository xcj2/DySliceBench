import sys
import copy
from io import StringIO
import unittest
from collections import deque

# 参考：https://atcoder.jp/contests/abc168/submissions/13401646

def resolve():
    n, m = map(int, input().split())
    ms = [list(map(int, input().split())) for i in range(m)]

    # 各部屋のつながりを整理整頓する(添え字0は使わないので、+1して一つ多い配列を作成)
    roots = [[] for i in range(n + 1)]
    for i in ms:
        roots[i[0]].append(i[1])
        roots[i[1]].append(i[0])

    # 各部屋の深さを保持する配列を作成(配列は0始まりだが、番号は1始まりなので+1(添え字0は使用しない想定))
    deeps = [99999 for i in range(n + 1)]
    aaa = [False for i in range(n + 1)]

    best_signs = [0 for i in range(n+1)]

    # 調べ終えた道を格納するタプル
    # searched = []

    # 初期値を代入
    que = deque()
    que.append(1)  # スタート地点
    deeps[1] = 0  # スタート地点の深さは0

    # BFS開始
    while not len(que) is 0:

        now = que.popleft()

        # 無限ループ防止のため調査済みフラグを立てる
        # searched.append(now)

        # 最適解を代入し続けて、適切な深さを求める
        for target in roots[now]:
            # 調査済みの道には何もしない。
            if aaa[target] is True:
                continue

            # 新しい道の場合。最適解を取得+キュー追加
            deeps[target] = deeps[now] + 1
            que.append(target)
            aaa[target] = True
            # 最適な道しるべを設定
            best_signs[target] = now

    # 不要な添え字を削除(0番目=未使用なので不要 1番目=出力しないので不要)
    # del best_signs[0:2]

    # ans = "Yes"
    print("Yes")
    for i in range(2, len(best_signs)):
        # ans = ans + "\n" + str(best_signs[i])
        print(best_signs[i])

    # print(ans)


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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
