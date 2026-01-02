# -*- coding: utf-8 -*-
from itertools import combinations_with_replacement


def read_int_n():
    return list(map(int, input().split()))


def slv(N, M, Q, ABCD):
    ans = 0
    for a in combinations_with_replacement(range(1, M+1), r=N):
        t = 0
        for abcd in ABCD:
            A, B, C, D = abcd
            if a[B-1] - a[A-1] == C:
                t += D
        ans = max(ans, t)
    return ans


def main():
    N, M, Q = read_int_n()
    ABCD = [read_int_n() for _ in range(Q)]
    print(slv(N, M, Q, ABCD))


if __name__ == '__main__':
    main()
