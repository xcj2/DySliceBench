#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int, X: "List[int]"):
    distance = []
    for i in range(1,N):
        distance.append(X[i]-X[i-1])
    
    answer =0 
    for d in distance:
        answer += min(d*A,B)
    print(answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, X)

if __name__ == '__main__':
    main()
