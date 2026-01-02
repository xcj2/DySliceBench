#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    answer = 0
    max_abc= max(A,B,C)

    answer += (max_abc-A)//2
    A = max_abc-int((max_abc-A)%2 != 0)
    answer += (max_abc-B)//2
    B = max_abc-int((max_abc-B)%2 != 0)
    answer += (max_abc-C)//2
    C = max_abc-int((max_abc-C)%2 != 0)

    if A == B == C:
        print(answer)
        return 

    if [A,B,C].count(max_abc) == 2:
        answer += 2
    else:
        answer += 1

    print(answer)

    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()
