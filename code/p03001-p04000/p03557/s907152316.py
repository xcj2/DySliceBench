#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    A.sort()
    C.sort()
    answer = 0
    for i in range(N):
        A_index = bisect.bisect_left(A,B[i])
        C_index = bisect.bisect_left(C,B[i]+1) 
        answer += (N-C_index)*A_index
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
