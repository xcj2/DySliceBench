#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, = read_h()
    A = read_h()

    if len(A) == 1:
        print(1)
        return

    cnt = 1
    inc = None

    for i in range(len(A) - 1):
        #  print(A[i:i + 2])

        if inc is None and A[i] != A[i + 1]:
            inc = A[i] < A[i + 1]
            continue

        if A[i] == A[i + 1] or (inc and A[i] < A[i + 1]) or (not inc and A[i] > A[i + 1]):
            continue

        #  print('change')
        cnt += 1
        inc = None

    print(cnt)


if __name__ == '__main__':
    main()
