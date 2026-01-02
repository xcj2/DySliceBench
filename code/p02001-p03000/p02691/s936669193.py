import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    a_s = list(map(int, input().split()))

    # sums = [i+1 - a_s[i] for i in range(len(a_s))]
    #
    # # ans = [sums[sums[i]-1:-1].count(sums[i]) for i in range(len(a_s))]
    #
    # ans = 0
    # for i in range(len(a_s)):
    #     ans += sums[a_s[i]-i-1:-1].count(a_s[i]+i+1)
    #
    # # print(sum(ans))
    # print(ans)

    # 「番号+身長」「番号-身長」の計算結果をまとめたリストを作成(dict型のイメージ。結果が1になるデータが2個ある,2になるデータが4個ある・・等)
    # a_plus_list = [0 for i in range(len(a_s)+1)]
    # a_minus_list = [0 for i in range(len(a_s)+1)]
    # for i in range(len(a_s)+1):
    #     a_plus_list[i+1 + a_s[i]] += 1
    #     # a_minus_list[i+1 - a_s[i]] += 1

    a_plus_dict = {}
    a_minus_dict = {}
    for i in range(len(a_s)):
        plus = a_plus_dict.get(i+1 + a_s[i], 0)
        a_plus_dict[i+1 + a_s[i]] = plus + 1

        if i+1 <= a_s[i]:
            continue

        minus = a_minus_dict.get(i+1 - a_s[i], 0)
        a_minus_dict[i+1 - a_s[i]] = minus + 1

    ans = 0
    for key, val in a_plus_dict.items():

        target = a_minus_dict.get(key, 0)
        ans += target * val

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
        input = """6
2 3 3 1 3 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6
5 2 4 2 8 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5"""
        output = """22"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()