import sys
from functools import reduce
from operator import mul
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


def mod_comb_init(max_: int) -> Callable[[Type[T]], Type[T]]:
    def _mod_comb_init(cls: Type[T]) -> Type[T]:
        mod: int = cls.mod
        assert max_ < mod

        fac = cls.fac = [0] * max_
        finv = cls.finv = [0] * max_
        inv = cls.inv = [0] * max_

        fac[0] = fac[1] = 1
        finv[0] = finv[1] = 1
        inv[1] = 1
        for i in range(2, max_):
            fac[i] = fac[i - 1] * i % mod
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            finv[i] = finv[i - 1] * inv[i] % mod

        return cls
    return _mod_comb_init


@mod_comb_init(2 * 10 ** 6 + 1)
class ModInt(ModIntBase):
    mod = 1000000007  # 10 ** 9 + 7


def resolve(in_):
    r1, c1, r2, c2 = map(int, next(in_).strip().split())
    # ans = f(r2+1, c2+1) - f(r2+1, c1) - f(r1, c2+1) + f(r1, c1)
    ans = (
        ModInt.comb((r2 + 1) + (c2 + 1), c2 + 1)
        - ModInt.comb((r2 + 1) + c1, c1)
        - ModInt.comb(r1 + (c2 + 1), c2 + 1)
        + ModInt.comb(r1 + c1, c1)
    )

    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
