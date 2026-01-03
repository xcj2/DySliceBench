#!/usr/bin/env python3
import sys


def solve(N: int, x: int, a: "List[int]"):
    answer =0
    for i in range(N-1):
        consum = a[i]+a[i+1]
        if consum > x:
            a[i+1]-= min(consum-x,a[i+1])
            answer+=consum-x
        
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x, a)

if __name__ == '__main__':
    main()
