import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

# grobalにmdを設定すること
class mint:
    def __init__(self, x):
        self.__x = x % md

    def __str__(self):
        return str(self.__x)

    def __neg__(self):
        return mint(-self.__x)

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

md = 10**9+7

def main():
    n,k=MI()
    dp=[mint(0) for _ in range(k+1)]
    for a in range(k,0,-1):
        dp[a]+=pow(k//a,n,md)
        for b in range(2*a,k+1,a):
            dp[a]-=dp[b]
    ans=0
    for a in range(1,k+1):
        ans+=dp[a]*a
    print(ans)

main()