from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


class ModInt(int):
    
    MOD = 7

    def __new__(cls, x, *args, **kwargs):
        return super().__new__(cls, x % ModInt.MOD)

    def __add__(self, other):
        return ModInt(super().__add__(other) % ModInt.MOD)
    
    def __radd__(self, other):
        return ModInt(super().__radd__(other) % ModInt.MOD)
    
    def __mul__(self, other):
        return ModInt(super().__mul__(other) % ModInt.MOD)
    
    def __rmul__(self, other):
        return ModInt(super().__rmul__(other) % ModInt.MOD)
    
    def __pow__(self, other, *args):
        return ModInt(super().__pow__(other, ModInt.MOD))

    def __rpow__(self, other, *args):
        raise NotImplementedError()
    
    def __truediv__(self, other):
        return ModInt(super().__mul__(pow(other, ModInt.MOD-2, ModInt.MOD)))
    
    def __floordiv__(self, other):
        return self.__truediv__(other)
    
    def __rtruediv__(self, other):
        return ModInt(self.__pow__(ModInt.MOD-2).__mul__(other))
    
    def __rfloordiv__(self, other):
        return self.__rtruediv__(other)


def read():
    ModInt.MOD = 10**9+7
    H, W = map(int, input().strip().split())
    M = []
    for i in range(H):
        M.append(input().strip())
    return H, W, M


def solve(H, W, M):
    dp = [ModInt(0) for i in range(W+1)]
    dp[1] = 1
    for i in range(1, H+1):
        for j in range(1, W+1):
            dp[j] = (dp[j] + dp[j-1]) if M[i-1][j-1]=='.' else 0
    return dp[W]


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
