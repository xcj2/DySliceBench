#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    f = [[False] * (N) for i in range(N)]
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if b[i] == A[j][k]:
                    f[j][k] = True
    t = False
    for i in range(3):
        if all([f[i][k] for k in range(3)]):
            t = True

    for i in range(3):
        if all([f[k][i] for k in range(3)]):
            t = True
    
    if all([f[k][k] for k in range(3)]):
        t = True

    if f[0][2] and f[1][1] and f[2][0]:
        t = True

    if t:
        print(YES)
    else:
        print(NO)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
