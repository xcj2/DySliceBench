MOD = 10**9 + 7
INF = 10**9 + 7


class modint():
    def __init__(self, value):
        self.value = value % MOD

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return (modint(self.value + other.value) if isinstance(other, modint)
                else modint(self.value + other))

    def __sub__(self, other):
        return (modint(self.value - other.value) if isinstance(other, modint)
                else modint(self.value - other))

    def __mul__(self, other):
        return (modint(self.value * other.value) if isinstance(other, modint)
                else modint(self.value * other))

    def __truediv__(self, other):
        return (modint(self.value * pow(other.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(self.value * pow(other, MOD - 2, MOD)))

    def __pow__(self, other):
        return (modint(pow(self.value, other.value, MOD))
                if isinstance(other, modint)
                else modint(pow(self.value, other, MOD)))

    def __eq__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __ne__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __radd__(self, other):
        return (modint(other.value + self.value) if isinstance(other, modint)
                else modint(other + self.value))

    def __rsub__(self, other):
        return (modint(other.value - self.value) if isinstance(other, modint)
                else modint(other - self.value))

    def __rmul__(self, other):
        return (modint(other.value * self.value) if isinstance(other, modint)
                else modint(other * self.value))

    def __rtruediv__(self, other):
        return (modint(other.value * pow(self.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(other * pow(self.value, MOD - 2, MOD)))

    def __rpow__(self, other):
        return (modint(pow(other.value, self.value, MOD))
                if isinstance(other, modint)
                else modint(pow(other, self.value, MOD)))

    def modinv(self):
        return modint(pow(self.value, MOD - 2, MOD))


def main():
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    ans = modint(1)
    if N == K:
        for a in A:
            ans *= a
        return print(ans)
    elif all(a < 0 for a in A) and K % 2 == 1:
        A.sort(key=abs)
        for a in A[:K]:
            ans *= a
        return print(ans)
    # 以降，非負の答えにできる
    A.sort(reverse=True, key=abs)
    if sum(a < 0 for a in A[:K]) % 2 == 0:
        for a in A[:K]:
            ans *= a
    else:
        ans1 = modint(1)  # 正を取り除く
        ans2 = modint(1)  # 負を取り除く
        p_remove = False
        x1 = INF
        for a in A[:K][::-1]:
            if a > 0 and not p_remove:
                p_remove = True
                x1 = a
                continue
            ans1 *= a
        n_remove = False
        x2 = INF
        for a in A[:K][::-1]:
            if a < 0 and not n_remove:
                n_remove = True
                x2 = a
                continue
            ans2 *= a
        y1 = 0  # 一番大きい負
        y2 = 0  # 一番大きい正
        for a in A[K:]:
            if y1 == 0 and a < 0:
                y1 = a
            if y2 == 0 and a > 0:
                y2 = a
            if y1 != 0 and y2 != 0:
                break
        ans1 *= y1
        ans2 *= y2
        if x1 != INF and x2 != INF:
            if abs(x2*y1) <= abs(x1*y2):
                ans = ans2
            else:
                ans = ans1
        elif x1 == INF and x2 == INF:
            # all 0
            ans = 0
        elif x1 == INF:
            # A[:K]に正の整数がなかった
            ans = ans2
        else:
            # A[:K]に負の整数がなかった
            # でもこれのときはif sum(a < 0 for a in A[:K]) % 2 == 0
            # がTrueになるからいらなそう？
            ans = ans1
    print(ans)


if __name__ == '__main__':
    main()
