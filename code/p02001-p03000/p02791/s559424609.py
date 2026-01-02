#!/usr/bin/env python3
import sys


def solve(N: int, P: "List[int]"):
    answer = 1
    cur_min = P[0]
    for i in range(1,N):
        if P[i] <= cur_min:
            answer += 1
        
        cur_min = min(cur_min,P[i])
    print(answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)

if __name__ == '__main__':
    main()
