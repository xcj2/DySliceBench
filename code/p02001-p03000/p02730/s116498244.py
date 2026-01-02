#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    N = len(S)

    if N == 3:
        if S == S[::-1]:
            print(YES)
            exit()
        else:
            print(NO)
            exit()

    s1 = S[:(N-1)//2]
    s1r = s1[::-1]
    s2 = S[(N+3)//2]
    s2r = s2[::-1]
    # print(s1, s1r, s2, s2r)
    if S == S[::-1] and s1 == s1r and s2 == s2r:
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
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
