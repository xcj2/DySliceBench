import sys
input = sys.stdin.readline


def read():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, K, A


class ModInt(int):
    
    MOD = 10**9+7

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


def solve(N, K, A):
    ModInt.MOD = 10**9+7
    N = len(A)
    k = ModInt(K)
    t0 = k * (k+1) // 2  # 三角数
    t1 = (k-1) * k // 2

    c0 = 0
    c1 = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                c0 += 1
            elif A[i] < A[j]:
                c1 += 1
    return c0 * t0 + c1 * t1


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
