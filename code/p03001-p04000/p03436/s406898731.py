import sys
from io import StringIO
import unittest
import queue


def resolve():
    # ★get input
    h, w = map(int, input().split())

    grid = [["" for i in range(w)] for j in range(h)]

    for i in range(h):
        line = input()
        for j in range(w):
            grid[i][j] = line[j:j+1]

    # ★exec
    # 最短経路を求める
    distance = [[-1 for i in range(w)] for j in range(h)]
    que = queue.Queue()

    # スタート地点の情報を設定
    que.put([0, 0])
    distance[0][0] = 0

    while not que.empty():

        now = que.get()

        # 上下左右のマスを確認
        for move_y, move_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):

            # 迷路の範囲外なら何もしない
            target = [now[0] + move_y, now[1] + move_x]
            if not h > target[0] >= 0 or not w > target[1] >= 0:
                continue

            # 黒塗りされているなら何もしない
            if grid[target[0]][target[1]] == '#':
                continue

            # 距離が設定済みなら何もしない
            if not distance[target[0]][target[1]] == -1:
                continue

            # キューに追加
            que.put(target)

            # 最短距離を設定
            distance[target[0]][target[1]] = distance[now[0]][now[1]] + 1

    # 最短経路までの距離を取得
    shortest_distance = distance[h-1][w-1]
    # 到達不可能の場合、ここで終了
    if shortest_distance == -1:
        print("-1")
        return

    # 塗りつぶしできないマスの個数を取得
    # 初期値1(スタート地点は塗りつぶし不可能であるため
    not_repaint_count = 1
    # 最初黒で塗られているマスの数を加算
    for i in range(h):
        not_repaint_count += grid[i].count("#")

    # 最初白のマス - 最短経路 = 塗りつぶしできるマス数。
    a = len(grid) * len(grid[0]) - not_repaint_count - shortest_distance
    print(a)


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
..#
#..
..."""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
....................................."""
        output = """209"""
        self.assertIO(input, output)

if __name__ == "__main__":
    resolve()