#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]", B: "List[int]"):
    a = A
    b = B
    a.sort()
    b.sort()
    if N % 2 == 0:
        ma = (a[N // 2 - 1] + a[N // 2]) / 2
        mb = (b[N // 2 - 1] + b[N // 2]) / 2
        ret = mb * 2 - ma * 2 + 1
    else:
        ma = (a[N // 2]) / 2
        mb = (b[N // 2]) / 2
        ret = mb * 2 - ma * 2 + 1
    print(int(ret))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
