import sys
from io import StringIO
import unittest

from collections import Counter

def resolve():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    end_flag = False

    # 全列挙 or 条件探索
    # if max([s for s, c in sc]) > n:
    #     end_flag = True
    #
    if n == 2 or n == 3:
        if [1, 0] in sc:
            end_flag = True
    #
    # for i in range(len(sc) - 1):
    #     if sum([1 for s, c in sc[i+1:] if s == sc[i][0] and c != sc[i][1]]) >= 1:
    #         end_flag = True
    #         break

    ans = [''] * n

    # メイン処理
    for s, c in sc:
        if ans[s - 1] == '' or ans[s - 1] == c:
            ans[s - 1] = c
        else:
            end_flag = True
            break

    # 埋まってない場所を埋める
    for i in range(len(ans)):
        if ans[i] == '':
            if i == 0 and n != 1:
                ans[i] = 1
            elif i == 0 and n == 1:
                ans[i] = 0
            elif i != 0:
                ans[i] = 0

    """
    n で桁数決め
    以下の通りならアウト
    - max_sがnより大きい
    - s, cの組み合わせが一致しない、sが複数出てくる
    - n == 2 or 3で頭が0
    
    それ以外の場合
    
        
    """

    if end_flag:
        print(-1)
    else:
        print(int(''.join(map(str, ans))))

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
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()