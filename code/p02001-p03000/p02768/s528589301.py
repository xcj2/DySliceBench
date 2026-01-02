import sys
from io import StringIO
import unittest
import math
# 検索用タグ、繰り返し2乗法、膨大な組み合わせ、フェルマーの小定理
# https://math.nakaken88.com/textbook/cp-binary-exponentiation-and-recursive-function/
# ちなみに、pythonでは(pow())にて実装済みなので、自作不要。
# https://note.com/keyem/n/n526ee14fe3de
# 「繰り返し2乗法」はプログラム数学とでも呼ぶべき分野(高校、大学数学とは多分違う。「プログラムに対してのみ」効果があるので・・)
# --------------------------------------------------
# この問題のポイントは・・「組み合わせをXの(y)-2乗」という形に変換する事。
# https://img.atcoder.jp/abc156/editorial.pdf
# https://qiita.com/ofutonfuton/items/92b1a6f4a7775f00b6ae
# 10億種類の花から10万個を選ぶ・・というのは処理速度的に無理だが、
# 「Xの?乗」という形に変換できれば、繰り返し2乗法で高速に計算できる!(pythonならpow()を使うだけでOK)
# --------------------------------------------------

# 膨大な組み合わせ(10億C10万とか)の数を求める関数。
def cmb(n, r):
    mod = 10**9+7
    ans = 1
    for i in range(r):
        ans *= n-i
        ans %= mod
    for i in range(1, r+1):
        ans *= pow(i, mod-2, mod)
        ans %= mod
    return ans

def resolve():

    n, a, b = map(int, input().split())

    # 10の9乗+7を算出しておく。
    div = pow(10, 9) + 7

    # 合計 = a,bを無視した総パターン数 - patternAの数 - patternbの数
    total = pow(2, n, div) - 1 - cmb(n, a) - cmb(n, b)
    print(total % div)

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
        input = """4 1 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1000000000 141421 173205"""
        output = """34076506"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()