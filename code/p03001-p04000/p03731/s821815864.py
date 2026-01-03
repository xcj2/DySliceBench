#!/usr/bin/env python3
import sys


def solve(N: int, T: int, t: "List[int]"):
    answer =0 
    for i in range(N-1):
        answer += min(t[i+1]-t[i],T)
    
    answer += T
    print(answer)


    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, t)

if __name__ == '__main__':
    main()
