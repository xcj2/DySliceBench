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


def inv(a, mod):
    return pow(a, mod - 2, mod)


def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod


def main():
    mod = 10 ** 9 + 7
    N, K = read_values()
    A = sorted(read_list())
    F = func(N, mod)
    res = 0
    t = N - 1
    c = C(F, N - 1, K - 1, mod)
    for i in range(N - K + 1):
        res += (A[- i - 1] - A[i]) * c % mod
        res %= mod
        c *= (t - K + 1) * inv(t, mod)
        c %= mod
        t -= 1

    print(res)

if __name__ == "__main__":
    main()

