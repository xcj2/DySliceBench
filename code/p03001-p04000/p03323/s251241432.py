#!/usr/bin/env python3
import sys

YES = "Yay!"
NO = ":("

def solve(A: int, B: int):
    m = "null"
    for i in range(16):
        if A == 0 and B == 0:
            break
        if i != 15:
            if A > 0 and m != "A":
                A -= 1
                m = "A"
            elif B > 0 and m != "B":
                B -= 1
                m = "B"
            else:
                m = "Brank"
        else:
            if B > 0 and m != "B":
                B -= 1

    if A == 0 and B == 0:
        print(YES)
    else:
        print(NO)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
