#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int, C: int):

    ans = 0
    while(A%2 == 0 and B%2 == 0 and C%2 == 0):
        oA, oB, oC = A, B, C
        A2, B2, C2 = A//2, B//2, C//2
        A = B2 + C2
        B = A2 + C2
        C = A2 + B2
        if A == oA and B == oB and C == oC:
            print('-1')
            exit()
        ans += 1

    print(ans)

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
