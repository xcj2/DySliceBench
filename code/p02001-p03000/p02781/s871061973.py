import sys
from functools import lru_cache

read = sys.stdin.read


def com(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    numer = denom = 1
    for i in range(n - r + 1, n + 1):
        numer = numer * i
    for i in range(1, r + 1):
        denom = denom * i
    return numer // denom


def main():
    N, K = map(int, read().split())

    S = str(N)
    L = len(S)

    @lru_cache(maxsize=None)
    def rec(i, k, smaller):
        if i == L:
            if k == 0:
                return 1
            else:
                return 0
        if k == 0:
            return 1
        if smaller:
            return com(L - i, k) * pow(9, k)
        if S[i] == '0':
            return rec(i + 1, k, False)

        ans = 0
        ans += rec(i + 1, k, True)
        ans += rec(i + 1, k - 1, True) * (int(S[i]) - 1)
        ans += rec(i + 1, k - 1, False)
        return ans

    ans = rec(0, K, False)

    print(ans)
    return


if __name__ == '__main__':
    main()
