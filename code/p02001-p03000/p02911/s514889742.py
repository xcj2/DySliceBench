#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, K: int, Q: int, A: "List[int]"):
    p = [0] * N
    for j in range(Q):
        p[A[j] - 1] += 1
    for i in range(N):
        if K - Q + p[i] > 0:
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
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(Q) ]  # type: "List[int]"
    solve(N, K, Q, A)

if __name__ == '__main__':
    main()
