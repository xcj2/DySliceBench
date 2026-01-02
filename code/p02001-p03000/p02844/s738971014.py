#!/usr/bin/env python3
import sys
INF = float("inf")


def z_algorithm(S):
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


def zfindall(text, pattern, separator="$"):
    N = len(pattern)
    conc = pattern+separator+text
    Z = z_algorithm(conc)

    umu = [i-N-1 for i in range(len(conc)) if Z[i] == N]
    return umu


def solve(N: int, S: str):

    len1 = [0]*10
    len2 = [0]*100
    len3 = [0]*1000
    for c in S:
        # 長さ3
        for i in range(100):
            if len2[i] > 0:
                len3[int(str(i)+c)] = 1

        # 長さ2
        for i in range(10):
            if len1[i] > 0:
                len2[int(str(i)+c)] = 1

        # 長さ1
        len1[int(c)] = 1
    counter = 0
    for i in range(1000):
        if len3[i] == 1:
            counter += 1

    print(counter)
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
