import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

MOD = 10 ** 9 + 7

N, M = list(map(int, sys.stdin.readline().split()))
X = list(map(int, sys.stdin.readline().split()))
Y = list(map(int, sys.stdin.readline().split()))


def ModInt(mod):
    class _ModInt:
        def __init__(self, value):
            self.value = value % mod

        def __add__(self, other):
            if isinstance(other, _ModInt):
                return _ModInt(self.value + other.value)
            else:
                return _ModInt(self.value + other)

        def __radd__(self, other):
            return self.__add__(other)

        def __mul__(self, other):
            if isinstance(other, _ModInt):
                return _ModInt(self.value * other.value)
            else:
                return _ModInt(self.value * other)

        def __truediv__(self, other):
            # TODO: 実装
            raise NotImplementedError()

        def __repr__(self):
            return str(self.value)

    return _ModInt


MI = ModInt(MOD)
X = np.diff(X)
Y = np.diff(Y)
X = np.array([MI(x) for x in X])
Y = np.array([MI(y) for y in Y])

#  あるエリアが何回カウントされるか
xc = np.arange(len(X), -len(X), -2).cumsum()
yc = np.arange(len(Y), -len(Y), -2).cumsum()

print(np.dot(X, xc) * np.dot(Y, yc))
