#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    num = 1
    for aa in a:
        if aa == num:
            num +=1
    
    if num == 1:
        print(-1)
    else:
        print(N-(num-1))
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
