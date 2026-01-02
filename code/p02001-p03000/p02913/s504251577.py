#!/usr/bin/env python3
import sys
INF = float("inf")


def z_algorithm(S):
    """Zアルゴリズム
    https://snuke.hatenablog.com/entry/2014/12/03/214243 の二番目のコード
    """
    N = len(S)
    Z = [0]*N

    c = 0
    for i in range(1, N):
        if i+Z[i-c] < c+Z[c]:
            Z[i] = Z[i-c]
        else:
            j = max(0, c+Z[c]-i)
            while i+j < N and S[j] == S[i+j]:
                j += 1
            Z[i] = j
            c = i
    Z[0] = len(S)
    return Z


def solve(N: int, S: str):

    ans = 0
    for i in range(N-1):        # N
        z = z_algorithm(S[i:])  # N
        for j, zz in enumerate(z):  # N
            ans = max(min(j, zz), ans)
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()
