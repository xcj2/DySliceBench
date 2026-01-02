#!/usr/bin/env python3
import sys
 
YES = "Yes"  # type: str
NO = "No"  # type: str
 
def solve(N: int, A: int, B: int, C: int, D: int, S: str):
    ret = YES
    if '##' in S[A - 1:C] or '##' in S[B - 1:D]:
        ret = NO
    else:
        if D < C:
            #if S[B - 2:B] == '..' or S[B - 1:B + 1] == '..':
            if not '...' in S[B - 2:D + 1]:
                ret = NO
    print(ret)
    return
 
 
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, A, B, C, D, S)
 
if __name__ == '__main__':
    main()