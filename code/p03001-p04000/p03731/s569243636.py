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
    N, T = read_values()
    A = read_list()
    res = T
    for i in range(N - 1):
        res += min(A[i + 1] - A[i], T)

    print(res)


if __name__ == "__main__":
    main()

