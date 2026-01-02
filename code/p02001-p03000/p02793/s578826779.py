import sys
from collections import Counter
from functools import reduce
from operator import mul, ior

from typing import Callable, ClassVar, Sequence, Type, TypeVar


T = TypeVar('T', bound='ModIntBase')


class ModIntBase:
    value: int
    mod: ClassVar[int]
    fac: ClassVar[Sequence[int]] = ()
    inv: ClassVar[Sequence[int]] = ()
    finv: ClassVar[Sequence[int]] = ()

    def __init__(self, value: int) -> None:
        self.value = value % self.mod

    def __hash__(self) -> int:
        return hash((self.value, self.mod))

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return NotImplemented

    def __ne__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.value != other.value
        else:
            return NotImplemented

    # TODO: Add type hints
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__((self.value + other.value) % self.mod)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__((self.value - other.value) % self.mod)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.value * other.value % self.mod)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            a = other.value
            b = self.mod
            u = 1
            v = 0
            while b:
                t = a // b
                a, b = b, a - t * b
                u, v = v, u - t * v
            return self.__class__(self.value * u % self.mod)
        else:
            return NotImplemented

    def __pow__(self, other):
        if isinstance(other, self.__class__):
            v = 1
            a = self.value
            b = other.value
            mod = self.mod
            while b > 0:
                if b & 1:
                    v = v * a % mod
                a = a * a % mod
                b >>= 1
            return self.__class__(v)
        else:
            return NotImplemented

    @classmethod
    def comb(cls, n: int, k: int):
        if n < k:
            return cls(0)
        if n < 0 or k < 0:
            return cls(0)

        if n < len(cls.fac):
            return cls(cls.fac[n] * (cls.finv[k] * cls.finv[n - k] % cls.mod) % cls.mod)
        else:
            k = min(k, n - k)
            a = reduce(mul, map(cls, range(n - k + 1, n + 1)), cls(1))
            b = reduce(mul, map(cls, range(1, k + 1)), cls(1))
            return a / b

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.value!r})'

    def __str__(self) -> str:
        return str(self.value)


class ModInt(ModIntBase):
    mod = 1000000007  # 10 ** 9 + 7


def prime_factor(a, temp):
    while a > 1:
        yield temp[a]
        a //= temp[a]


def resolve(in_):
    N = int(next(in_))
    A = tuple(map(int, next(in_).split()))

    max_a = max(A)
    temp = [0] * (max_a + 1)
    temp[1] = 1

    for i in range(2, max_a + 1):
        if temp[i]:
            continue

        for j in range(i, max_a + 1, i):
            temp[j] = i
    
    ap_list = (Counter(prime_factor(a, temp)) for a in A)
    lcm = reduce(ior, ap_list, Counter())
    lcm_i = ModInt(1)
    for v in lcm.elements():
        lcm_i *= ModInt(v)


    ans = ModInt(0)
    for a in A:
        ans += lcm_i / ModInt(a)

    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
