import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    t = input()

    # 初期値の設定(結果が偽の場合の値を初期値にしてしまう)
    ans = "UNRESTORABLE"

    # i文字目から代入した場合、を検証していく
    for i in range(len(s)-len(t)+1):

        # iから一文字ずつ、不正な点が無いか検証。

        for j in range(len(t)):
            isRestorable = True

            if not s[j+i] == t[j] and not s[j+i] == "?":
                isRestorable = False
                break

        # 文字が代入できるなら、代入した場合の文字を変数に入れる。
        # これをループしていくので、ansには最終的に、辞書最小値が格納される、というロジック。
        if isRestorable:
            ans = s[0:i] + t + s[i+len(t):len(s)]
            ans = ans.replace("?", "a")

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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()