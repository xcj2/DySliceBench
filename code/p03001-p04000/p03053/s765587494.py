import sys
from io import StringIO
import unittest
from collections import deque
# import queue


def resolve():
    # ★get input
    h, w = map(int, input().split())

    # grid = [["" for i in range(w)] for j in range(h)]
    # grid = [[-1 for i in range(w)] for j in range(h)]

    #for i in range(h):
    #    # grid[i] = list(input())
    #    grid[i] = list(input())

        # 以下の様にsliceで取得することもできるが、パフォーマンスが若干落ちる。
        # 1000×1000件で50ミリ秒くらい差が出る?
        # line = input()
        # for j in range(w):
        #     grid[i][j] = line[j:j+1]


    # ★exec
    # BFSにて最短経路を求める
    # 準備
    # distance = [[-1 for i in range(w)] for j in range(h)]
    distance = [[-1 for i in range(w)] for j in range(h)]
    # que = queue.Queue()
    que = deque()

    # スタート地点の情報を設定
    # 多点スタートの設定
    for i in range(h):
        line = list(input())
        for j in range(w):
            if line[j] == "#":
                # que.put((i, j))
                que.append((i, j))
                distance[i][j] = 0

    # BFS開始
    while len(que) > 0:

        # now = que.get()
        now = que.popleft()

        # 上下左右のマスを確認
        for move_y, move_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):

            # 盤の範囲外なら何もしない
            target = (now[0] + move_y, now[1] + move_x)
            if not (h > target[0] >= 0 and w > target[1] >= 0):
                continue

            # 黒塗りされているなら何もしない
            # この条件、不要な気がする・・
            # if grid[target[0]][target[1]] == '#':
            #     continue

            # 距離が設定済みなら何もしない
            if not distance[target[0]][target[1]] == -1:
                continue

            # キューに追加
            # que.put(target)
            que.append(target)
            # 最短距離を設定
            distance[target[0]][target[1]] = distance[now[0]][now[1]] + 1

            # 黒塗り
            # この処理、不要な気がする・・
            # grid[target[0]][target[1]] = '#'

    # 距離が最大の点 = 答えになる。
    ans = 0
    for i in range(h):
        ans = max(ans, max(distance[i]))

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
        input = """3 3
...
.#.
..."""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 6
..#..#
......
#..#..
......
.#....
....#."""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    resolve()