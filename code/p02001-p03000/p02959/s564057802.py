#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]", B: "List[int]"):
    ret = 0
    for i in range(N):
        if A[i] <= B[i]:
            B[i] -= A[i]
            ret += A[i]
            tmp = min(A[i + 1], B[i])
            #print(B[i], tmp)
            A[i + 1] -= tmp
            ret += tmp
        else:
            A[i] -= B[i]
            ret += B[i]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N+1) ]  # type: "List[int]"
    B = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
