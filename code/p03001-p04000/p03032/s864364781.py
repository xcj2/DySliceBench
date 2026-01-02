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


def f(V, L, R):
    import bisect
    N = len(V)
    
    res = 0
    for r in range(min(N - L, R) + 1):
        LL = sorted(V[:L] + V[-r:] if r != 0 else V[:L])
        k = min(R - r, bisect.bisect_left(LL, 0))
        res = max(res, sum(LL[k:]))
    return res


def main():
    N, K = read_values()
    V = read_list()
    
    res = 0
    for L in range(K + 1):
        res = max(res, f(V, L, K - L))
    print(res)


if __name__ == "__main__":
    main()

