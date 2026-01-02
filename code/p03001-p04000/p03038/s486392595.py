#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):

    BC = [[B[i], C[i]] for i in range(M)]
    BC = sorted(BC, key=lambda x:x[1], reverse=True)
    
    idx = 0
    A.sort()

    for i in range(N):
        if idx < M and BC[idx][0] > 0 and A[i] < BC[idx][1]:
            A[i] = BC[idx][1]
            BC[idx][0] -= 1
            if(BC[idx][0] == 0):
                idx += 1        


    print(sum(A))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
