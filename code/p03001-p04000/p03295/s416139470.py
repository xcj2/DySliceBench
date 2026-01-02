import sys
from io import StringIO
import unittest


def resolve():
    # ★get input
    n, m = map(int, input().split())

    demands = [[int(i) for i in input().split()] for j in range(m)]

    # 要望を[1]の昇順で並べ替え(後述する[1]-1の場所に橋を作る、という方法の効率を最大化するため、らしい。
    # 右側から徐々に橋を取り除くイメージ。
    demands = sorted(demands,key=lambda x:x[1])

    # 最後に取り除いた橋
    new_remove_bridge = 0
    # 取り除いた橋の数
    remove_bridge_count = 0

    for demand in demands:

        # 最後に取り除いた橋では分断できない島に対する要望を受けた場合
        # 例
        # 島1-除-島2-除-島3----島4 <= 2-3間の橋を取り除いた状態で・・3-4間の橋を取り除いてほしい、と言われた場合。
        if new_remove_bridge  < demand[0]:
            new_remove_bridge = demand[1] -1
            remove_bridge_count += 1

    print(str(remove_bridge_count))



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
        input = """5 2
1 4
2 5"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """9 5
1 8
2 7
3 5
4 6
7 9"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()