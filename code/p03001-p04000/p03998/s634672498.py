#!/usr/bin/env python3
import sys


def solve(S_A: str, S_B: str, S_C: str):
    a_index = 0
    b_index = 0
    c_index = 0
    cur = 'a'
    while True:
        if cur == "a":
            if a_index < len(S_A):
                cur = S_A[a_index]
                a_index += 1
            else:
                print('A')
                return
        elif cur == "b":
            if b_index < len(S_B):
                cur = S_B[b_index]
                b_index += 1
            else:
                print('B')
                return
        elif cur == "c":
            if c_index < len(S_C):
                cur = S_C[c_index]
                c_index += 1
            else:
                print('C')
                return

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S_A = next(tokens)  # type: str
    S_B = next(tokens)  # type: str
    S_C = next(tokens)  # type: str
    solve(S_A, S_B, S_C)

if __name__ == '__main__':
    main()
