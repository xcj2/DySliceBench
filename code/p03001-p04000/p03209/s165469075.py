import sys
from functools import lru_cache
def input(): return sys.stdin.readline().strip()


def main():
    N, X = map(int, input().split())

    @lru_cache(maxsize=None)
    def func(n, x):
        if n == 0:
            if x <= 0: return 0
            if x >= 1: return 1
        if x >= 2 ** (n + 2) - 3:
            return func(n - 1, x) * 2 + 1
        if x >= 2 ** (n + 1) - 1:
            return func(n - 1, x) + 1 + func(n - 1, x - (2 ** (n + 1) - 1))
        if x >= 1:
            return func(n - 1, x - 1)
        return 0

    print(func(N, X))




if __name__ == "__main__":
    main()
