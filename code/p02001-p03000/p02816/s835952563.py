#!/usr/bin/env python3
import sys


def z_algorithm(S):
    """Zアルゴリズム
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
    Z[0] = N
    return Z


def solve(N: int, a: "List[int]", b: "List[int]"):

    a1 = [0]*(2*N)
    b1 = [0]*N
    b2 = [0]*N
    k_cand = [True]*N
    for keta in range(30):
        for i, aa in enumerate(a):
            a1[i] = a1[i+N] = (aa >> keta) & 1
        for i, bb in enumerate(b):
            b1[i] = v = (bb >> keta) & 1
            b2[i] = 1-v
        Z1 = z_algorithm(b1 + [-1] + a1)
        Z2 = z_algorithm(b2 + [-1] + a1)
        # print(a1+[-1]+b1)
        # print(a1+[-1]+b2)
        # print("Z1", Z1)
        # print("Z2", Z2)
        for i in range(N):
            if k_cand[i]:
                k_cand[i] = Z2[i+N+1] == N or Z1[i+N+1] == N
        # print(k_cand)

    for i in range(N):
        if k_cand[i]:
            print(i, b[0] ^ a[i])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, a, b)


if __name__ == '__main__':
    main()
