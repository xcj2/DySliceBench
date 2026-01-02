#!/usr/bin/python3

import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, A):
    allxor = 0
    for a in A:
        allxor ^= a

    while len(A) < 61:
        A.append(0)
    M = len(A)

    row = 0
    ans = 0
    for bi in range(61, -1, -1):
        b = 1 << bi
        if b & allxor:
            ans |= b
            continue

        if not (A[row] & b):
            j = -1
            for i in range(row + 1, M):
                if A[i] & b:
                    j = i
                    break
            if j == -1:
                continue

            A[row], A[j] = A[j], A[row]

        assert A[row] & b
        if not (ans & b):
            ans ^= A[row]

        for i in range(row + 1, M):
            if A[i] & b:
                A[i] ^= A[row]
            assert not (A[i] & b)

        row += 1

    return ans + (ans ^ allxor)


def main():
    N = int(inp())
    A = [int(e) for e in inp().split()]
    print(solve(N, A))


if __name__ == '__main__':
    main()
