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


INV = dict()
def inv(a, mod):
    if a in INV:
        return INV[a]
    i = pow(a, mod - 2, mod)
    INV[a] = i
    return i 


def C(F, a, b, mod):
    return F[a] * inv(F[a - b], mod) * inv(F[b], mod) % mod 


def main():
    N, K = read_values()
    mod = 10 ** 9 + 7
    F = functional(5 * 10 ** 5, mod)
    res = 0
    if N <= K:
        res = C(F, 2 * N - 1, N - 1, mod)
    else:
        c = C(F, N - 1, 0, mod)
        for k in range(K + 1):
            res += pow(c, 2, mod) * N * inv(N - k, mod) % mod
            c *= ((N - k - 1) * inv(k + 1, mod)) % mod
            c %= mod
    
    print(res % mod)

if __name__ == "__main__":
    main()