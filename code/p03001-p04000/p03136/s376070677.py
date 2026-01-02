#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, L: "List[int]"):
    L.sort()
    if L[-1] < sum(L[:-1]):
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
    L = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, L)

if __name__ == '__main__':
    main()
