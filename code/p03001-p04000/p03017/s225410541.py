#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: int, B: int, C: int, D: int, S: str):
    
    if A<C<B<D:
        for i in range(A-1,C-1):
            if S[i] == S[i+1] == "#":
                print(NO)
                return
        for i in range(B-1,D-1):
            if S[i] == S[i+1] == "#":
                print(NO)
                return     
        print(YES)
        return
    
    if A<B<C<D:
        for i in range(A-1,C-1):
            if S[i] == S[i+1] == "#":
                print(NO)
                return
        for i in range(B-1,D-1):
            if S[i] == S[i+1] == "#":
                print(NO)
                return     
        print(YES)
        return

    if A<B<D<C:
        for i in range(B-1,D):
            if S[i-1] == S[i] == S[i+1] == ".":
                print(YES)
                return   
        print(NO)
        return     

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
