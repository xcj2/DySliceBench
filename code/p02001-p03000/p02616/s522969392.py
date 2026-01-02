# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
MOD = 10**9 + 7
def main(N, K, A):
    neg = pos = zer = 0
    for a in A:
        if a < 0: neg += 1
        elif a > 0: pos += 1
        else: zer += 1
    # print(neg, pos, zer, N - K)

    if N - K < zer:
        # ゼロになっちゃう
        return 0
    N -= zer
    A = sorted([a for a in A if a != 0], key=lambda x: abs(x))

    if (pos == 0 and K & 1) or (neg & 1 and N == K):
        # マイナスになっちゃう
        if zer:
            # ゼロにもできるじゃん
            return 0
        else:
            ans = Mint(1)
            for i in range(K):
                ans *= abs(A[i])
            return -ans

    # プラスにできる
    A.reverse()
    positives = []
    negatives = []
    # 絶対値の大きい方からK個取る
    for i in range(K):
        if A[i] > 0: positives.append(A[i])
        else: negatives.append(A[i])

    if len(negatives) & 1:
        # マイナスになっちゃった
        # マイナスを1手戻す
        nn = [negatives.pop()]
        pp = []
        rem = 1
        if positives:
            # プラスも1手戻す
            pp.append(positives.pop())
            rem = 2

        # 残りの人たちを探索
        for i in range(K, N):
            if A[i] < 0: nn.append(A[i])
            else: pp.append(A[i])
        # print(pp[:5])
        # print(nn[:5])

        if rem == 2:
            # マイナスのペアかプラスのペアを作る
            if len(nn) >= 2 and len(pp) < 2:
                # マイナスのペアだけ作れる
                negatives.append(nn[0])
                negatives.append(nn[1])
            elif len(pp) >= 2 and len(nn) < 2:
                # プラスのペアだけ作れる
                positives.append(pp[0])
                positives.append(pp[1])
            elif len(pp) >= 2 and len(nn) >= 2:
                # どっちも作れるなら掛けて大きい方
                if pp[0] * pp[1] > nn[0] * nn[1]:
                    positives.append(pp[0])
                    positives.append(pp[1])
                else:
                    negatives.append(nn[0])
                    negatives.append(nn[1])
            else:
                # どっちも作れないなんてことはない
                assert False
        else:
            # プラスをもう一つ選ぶ
            positives.append(pp[0])

    # 答えを計算
    ans = Mint(1)
    for p in positives:
        ans *= p
    for n in negatives:
        ans *= abs(n)
    return ans

class Mint:
    def __init__(self, value=0):
        self.value = value % MOD
        if self.value < 0: self.value += MOD

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % MOD
        return self

    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other)) % MOD
        if self.value < 0: self.value += MOD
        return self

    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj

    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % MOD
        return self

    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self

    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj

    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj //= self
        return new_obj

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *A, = map(int, input().split())
    print(main(N, K, A))
