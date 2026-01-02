import sys
from io import StringIO
import unittest

def resolve():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    bridges = [list(map(int, input().split())) for i in range(m)]

    # 結果を保持する配列
    bests = [True for i in range(n)]

    # 処理開始
    for bridge in bridges:

        bridge[0] -= 1
        bridge[1] -= 1

        if heights[bridge[0]] > heights[bridge[1]]:
            bests[bridge[1]] = False
        elif heights[bridge[0]] < heights[bridge[1]]:
            bests[bridge[0]] = False
        else:
            bests[bridge[1]] = False
            bests[bridge[0]] = False

    print(bests.count(True))


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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()