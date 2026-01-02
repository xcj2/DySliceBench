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


def main():
    N, M, Q = read_values()
    S = [[0 for _ in range(N + 1)] for __ in range(N + 1)]
    
    for _ in range(M):
        l, r = read_values()
        S[l][r] += 1

    for l in range(N):
        for r in range(N):
            S[l + 1][r + 1] += S[l + 1][r] + S[l][r + 1] - S[l][r] 

    res = [0] * Q
    for i in range(Q):
        p, q = read_values()
        res[i] = str(S[q][q] - S[p - 1][q] - S[q][p - 1] + S[p - 1][p - 1])
    print("\n".join(res))


if __name__ == "__main__":
    main()