#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, H: "List[int]", A: "List[int]", B: "List[int]"):
    conns = [[] for _ in range(N)]
    ret = 0
    for i in range(M):
        conns[A[i] - 1].append(B[i] - 1)
        conns[B[i] - 1].append(A[i] - 1)
    for i in range(N):
        tmp = 0
        for con in conns[i]:
            if H[i] > H[con]:
                tmp += 1
        if tmp == len(conns[i]) or len(conns[i]) == 0:
            ret += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    X = []
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, H, A, B)

if __name__ == '__main__':
    main()
