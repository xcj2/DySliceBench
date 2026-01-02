def main():
    N, M = map(int, input().split())
    lr = [
        list(map(int, input().split()))
        for _ in range(M)
    ]

    ans = f(N, M, lr)
    #ans = WA2(N, M, lr)
    #ans = TLE(N, M, lr)
    print(ans)


def WA(N, M, lr):
    import numpy as np
    a = np.zeros(N, dtype=int)
    for L, R in lr:
        a[L-1:R] += 1
    ans = (a == M).sum()
    return ans


def f(N, M, lr):
    l_max = max(L for L, _ in lr)
    r_min = min(R for _, R in lr)

    ans = r_min - l_max + 1
    ans = max(ans, 0)
    return ans


def TLE(N, M, lr):
    ans = 0
    for i in range(1, N+1):
        g = 0
        for L, R in lr:
            if L <= i <= R:
                g += 1
        if g == M:
            ans += 1

    return ans


if __name__ == '__main__':
    main()
