#  Copyright: this code was written at 2020. for AtCoder by Silviase

# Lib
import math


def mod_comb(n1, n2):
    return fac_tab[n1] * fac_tab[n2].inv() * fac_tab[n1 - n2].inv()


class ModInt:
    MOD = int(1e9 + 7)

    # int (演算子) ModIntはダメ

    def __init__(self, x):
        self.x = x % self.MOD

    # ModInt(op){ModInt, Int}に対応している
    def __add__(self, other):
        return self.__class__((self.x + other.x) % self.MOD) if isinstance(other, ModInt) else self.__class__(
            (self.x + other) % self.MOD)

    def __sub__(self, other):
        return self.__class__((self.x - other.x) % self.MOD) if isinstance(other, ModInt) else self.__class__(
            (self.x - other) % self.MOD)

    def __mul__(self, other):
        return self.__class__((self.x * other.x) % self.MOD) if isinstance(other, ModInt) else self.__class__(
            (self.x * other) % self.MOD)

    # 逆元をかけることに等しい
    def __truediv__(self, other):
        return self.__mul__(other.inv()) if isinstance(other, ModInt) else self.__mul__(ModInt(other).inv())

    # powは第三引数まで指定することで最適化される
    def __pow__(self, power, Modulo=MOD):
        return self.__class__(pow(self.x, power, Modulo))

    def _fac(self):
        mx = ModInt(1)
        for _i in range(self.x, 1, -1):
            mx = mx * _i
        return mx

    # mi_C_kをModInt型で返す
    def _comb(self, _k):
        if isinstance(_k, ModInt):
            if self < _k:
                return ModInt(0)
            return self._fac() * _k._fac().inv() * (self - _k)._fac().inv()
        else:
            if self < _k:
                return ModInt(0)
            return self._fac() * ModInt(_k)._fac().inv() * ModInt(self.x - _k)._fac().inv()

    def inv(self):
        return self.__pow__(self.MOD - 2)

    def __str__(self):
        return str(self.x)

    def __lt__(self, other):
        return self.x < other.x if isinstance(other, ModInt) else self.x < other


# Lib

# Code
# 素因数分解はルートまで,それ以上で残ったら一つ追加していけばいいことがわかる
# 各素因数についてx個あるのであれば(n+x)Cxであればいいことがわかる
# factに関しては毎回計算すると爆発するのでtableを持っておけばいいことがわかる
n, k = map(int, input().split())
result = ModInt(1)
fac_tab = [ModInt(1)] * 200000
for i in range(1, len(fac_tab)):
    fac_tab[i] = fac_tab[i - 1] * i

for i in range(2, int(math.sqrt(k) + 1)):
    tmp_cnt = 0
    while k % i == 0:
        k /= i
        tmp_cnt += 1
    result = result * mod_comb(n + tmp_cnt - 1, tmp_cnt)
    # print(result)

if k != 1:
    result = result * n
print(str(result))
