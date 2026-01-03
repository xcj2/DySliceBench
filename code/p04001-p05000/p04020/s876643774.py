#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]"):
    A.append(0)
    answer = 0
    for i in range(N):
        answer += A[i]//2
        A[i] %= 2
        if A[i] > 0 and A[i+1] > 0:
            A[i+1] -= 1
            answer += 1

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
    solve(N, A)

if __name__ == '__main__':
    main()
