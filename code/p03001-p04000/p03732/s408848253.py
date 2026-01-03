import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def func(N, mod):
    F = [1]
    for i in range(1, N + 1):
        F.append(F[-1] * i % mod)
    return F


INV = {}


def inv(a, mod):
    if a in INV:
        return INV[a]
    r = pow(a, mod - 2, mod)
    INV[a] = r
    return r


def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod


def main():
    N, W = read_values()
    dp = [
        [[0 for _ in range(N * 3 + 10)] for __ in range(N + 10)]
        for ___ in range(N + 10)
    ]
    I = [tuple(read_values()) for _ in range(N)]

    w0 = I[0][0]
    if w0 > W:
        print(0)
        return

    for i, (w1, v) in enumerate(I):
        w = w1 - w0
        for k in range(N):
            for j in range(N * 3 + 5):
                dp[i + 1][k][j] = max(dp[i][k][j], dp[i + 1][k][j])
                dp[i + 1][k + 1][j + w] = max(dp[i][k][j] + v, dp[i + 1][k + 1][j + w])

    res = 0
    for k in range(N + 1):
        r = min(W - k * w0, 3 * N + 5)
        if r < 0:
            continue
        for i in range(r + 1):
            res = max(res, dp[N][k][i])
    print(res)


if __name__ == "__main__":
    main()

