#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, a: "List[int]"):
    left_sum = list(itertools.accumulate(a))
    right_sum = list(itertools.accumulate(a[::-1]))

    answer = 2*10**9
    for i in range(N-1):
        answer = min(answer,abs(left_sum[i]-right_sum[N-2-i]))
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
