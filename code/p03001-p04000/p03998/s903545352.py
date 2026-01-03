#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S_A: str, S_B: str, S_C: str):
    S = [S_A, S_B, S_C]
    l = [len(S_A), len(S_B), len(S_C)]
    ith = [0, 0, 0]
    turn = 0

    while True:
        tt = ith[turn]
        if tt >= l[turn]:
            win = turn
            break
        k = ord(S[turn][tt])-ord('a')
        ith[turn] += 1
        turn = k
        # print(ith, turn)

    print("ABC"[win])
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
