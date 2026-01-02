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

    def __pow__(self, power, modulo=None):
        return mint(pow(self.__x, power, md))

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

md = 10 ** 9 + 7
def main():
    n = II()
    aa = LI()
    l = 1
    for a in aa:
        l = lcm(l, a)
    l = mint(l)
    ans = sum(l / a for a in aa)
    print(ans)

main()
