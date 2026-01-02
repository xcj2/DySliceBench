import sys
from io import StringIO
import unittest


def resolve():
    h, w = map(int, input().split())
    sw = [list(input()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            np_sharp = False
            if sw[i][j] == '#':
                for add_i, add_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_i = i + add_i
                    next_j = j + add_j

                    if next_i < 0 or next_j < 0 or h <= next_i or w <= next_j:
                        continue
                    else:
                        # 1つでも#があればOK
                        # すべて.だとNG
                        if sw[next_i][next_j] == '#':
                            np_sharp = True

                if not np_sharp:
                    print('No')
                    return
            else:
                continue

    print('Yes')



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
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
