#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, A: "List[int]"):
    A.sort()
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            print(NO)
            return
    print(YES)
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
