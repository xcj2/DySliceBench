import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def read_values():
    return map(int, input().split())


def read_index():
    return map(lambda x: x - 1, map(int, input().split()))


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def functional(N, mod):
    F = [1] * (N + 1)
    for i in range(N):
        F[i + 1] = (i + 1) * F[i] % mod
    return F


def inv(a, mod):
    return pow(a, mod - 2, mod)


def P(a, b, mod):
    res = 1
    for i in range(a, b + 1):
        res *= i
        res %= mod
    return res


def C(a, b, mod):
    return P(a - b + 1, a, mod) * inv(P(1, b, mod), mod) % mod


def main():
    N, A, B = read_values()
    mod = 10 ** 9 + 7 
    res = pow(2, N, mod) - 1

    p1 = P(N - A + 1, N, mod)
    p2 = p1 * P(N - B + 1, N - A, mod) % mod
    p3 = P(1, A, mod)
    p4 = p3 * P(A + 1, B, mod) % mod
    res -= p1 * inv(p3, mod) % mod
    res -= p2 * inv(p4, mod) % mod
    print(res % mod)


if __name__ == "__main__":
    main()