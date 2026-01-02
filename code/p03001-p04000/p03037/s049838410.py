def main():
    N, M = map(int, input().split())
    LR = [
        list(map(int, input().split()))
        for _ in range(M)
    ]

    ans = f(N, M, LR)
    ans1 = cumsum(N, M, LR)
    assert ans == ans1
    # ans = WA(N, M, LR)
    # ans = TLE(N, M, LR)
    print(ans)


def cumsum(N, M, LR):
    a = [0] * (N + 1)
    for L, R in LR:
        a[L-1] += 1
        a[R] -= 1

    from itertools import accumulate
    a = accumulate(a)
    ans = sum(x == M for x in a)
    return ans


def WA(N, M, LR):
    import numpy as np
    a = np.zeros(N, dtype=int)
    for L, R in LR:
        a[L-1:R] += 1
    ans = (a == M).sum()
    return ans


def f(N, M, LR):
    l_max = max(L for L, _ in LR)
    r_min = min(R for _, R in LR)

    ans = r_min - l_max + 1
    ans = max(ans, 0)
    return ans


def TLE(N, M, LR):
    ans = 0
    for i in range(1, N+1):
        g = 0
        for L, R in LR:
            if L <= i <= R:
                g += 1
        if g == M:
            ans += 1

    return ans


if __name__ == '__main__':
    main()
