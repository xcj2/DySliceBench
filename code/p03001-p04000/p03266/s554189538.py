def main():
    """
    1 <= N, K <= 2 * 10^5

    a,b,c (ok: a=b=c)

    """
    N, K = map(int, input().split())
    ans = f(N, K)
    assert ans == loop(N, K)
    # ans = TLE(N, K)
    print(ans)


def f(N, K):
    """
    1: a + b = l * K
    2: b + c = n * K
    3: c + a = m * K

    1 + 2 = c + a + 2b = (l + n) * K, 2b = (l + n - m) * K
    2 + 3 = a + b + 2c = (n + m) * K, 2c = (n + m - l) * K
    3 + 1 = b + c + 2a = (m + l) * K, 2a = (m + l - n) * K

    K % 2 == 0
        b = (l + n - m) * K / 2 = 整数
        Kの倍数 or K / 2 の倍数
    K % 2 == 1
        b = (l + n - m) * K / 2 = not 整数
        Kの倍数
    """
    if K % 2 == 1:
        # K の倍数の個数(N>=1より)
        x = N // K
        ans = x ** 3
    else:
        x1 = N // K
        x2 = (N + K // 2) // K
        ans = x1 ** 3 + x2 ** 3

    return ans


def loop(N, K):
    x = [0] * K
    for i in range(1, N+1):
        # K で割ったあまりがある値になる1-Nまでの個数
        x[i % K] += 1

    res = 0
    for a in range(K):
        # a余る数, K-a余る数(a=0 のときb=c=Kなので余りにする)
        b = (K - a) % K
        c = (K - a) % K

        if (b + c) % K == 0:
            res += x[a] * x[b] * x[c]

    return res


def TLE(N, K):
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                if (a + b) % K == 0 and \
                    (b + c) % K == 0 and \
                        (c + a) % K == 0:
                    ans += 1
    return ans


if __name__ == '__main__':
    main()
