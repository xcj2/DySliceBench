
import numpy as np


# 解がマイナスのとき
def solve1(k, ml, pl):
    left, right = -(10 ** 18) - 1, 0
    while right - left > 1:
        x = (left + right) // 2
        n = (len(pl) - np.searchsorted(pl, x // ml + (x % ml != 0))).sum()
        if k <= n:
            right = x
        else:
            left = x
    return right


# 解がプラスのとき
def solve2(k, ml, pl):
    left, right = 0, 10 ** 18
    while right - left > 1:
        x = (left + right) // 2
        n = 0
        n += (len(ml) - np.searchsorted(ml, x // ml + (x % ml != 0))).sum()
        n -= np.count_nonzero(ml ** 2 <= x)
        n += (np.searchsorted(pl, x // pl, side="right")).sum()
        n -= np.count_nonzero(pl ** 2 <= x)
        assert n % 2 == 0
        n //= 2
        if k <= n:
            right = x
        else:
            left = x
    return right


def main():
    N, K = list(map(int, input().split()))
    A = np.array(input().split(), dtype=int)
    A.sort()
    ml = A[A < 0]
    pl = A[A > 0]
    zl = A[A == 0]
    mn = len(ml) * len(pl)
    zn = sum([N - i - 1 for i in range(len(zl))])
    if K <= mn:
        ans = solve1(K, ml, pl)
    elif K <= mn + zn:
        ans = 0
    else:
        ans = solve2(K - mn - zn, ml, pl)
    print(ans)


if __name__ == "__main__":
    main()
