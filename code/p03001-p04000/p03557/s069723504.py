#!/usr/bin/env python3
import sys
from bisect import bisect_left,bisect_right

def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    answer = 0
    A.sort()
    C.sort()
    for i in range(N):
        answer += bisect_left(A,B[i])*(N-bisect_right(C,B[i]))
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)

if __name__ == '__main__':
    main()
