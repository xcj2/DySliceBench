#!/usr/bin/env python3
import sys


def solve(N: int, M: int, Q: int, L: "List[int]", R: "List[int]", p: "List[int]", q: "List[int]"):
    matrix = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        matrix[L[i]][R[i]] += 1
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            matrix[i][j] += matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
    
    for i in range(Q):
        pp,qq = p[i],q[i]
        print(matrix[qq][qq]-matrix[pp-1][qq]-matrix[qq][pp-1]+matrix[pp-1][pp-1])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    q = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    solve(N, M, Q, L, R, p, q)

if __name__ == '__main__':
    main()
