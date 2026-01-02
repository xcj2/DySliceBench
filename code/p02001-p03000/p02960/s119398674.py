import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class mint:
    def __init__(self, x):
        self.__x = x % md

    def __str__(self):
        return str(self.__x)

    def __add__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x + other)

    def __sub__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x - other)

    def __rsub__(self, other):
        return mint(other - self.__x)

    def __mul__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x * other)

    __radd__ = __add__
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x * pow(other, md - 2, md))

    def __rtruediv__(self, other):
        return mint(other * pow(self.__x, md - 2, md))

    def __pow__(self, power, modulo=None):
        return mint(pow(self.__x, power, md))

md = 10 ** 9 + 7

def main():
    s = SI()
    n = len(s)
    dp = [[0] * 13 for _ in range(n + 1)]
    # dp[i][m]...iケタ目までみたときに、余りがmになる数の個数
    dp[0][0] = mint(1)
    e10 = 1
    for i, c in enumerate(s[::-1]):
        for m in range(13):
            pre = dp[i][m]
            if pre == 0: continue
            if c == "?":
                for d in range(10):
                    nm = (m + d * e10) % 13
                    dp[i + 1][nm] += pre
            else:
                nm = (m + int(c) * e10) % 13
                dp[i + 1][nm] += pre
        e10 = e10 * 10 % 13
    print(dp[n][5])

main()
