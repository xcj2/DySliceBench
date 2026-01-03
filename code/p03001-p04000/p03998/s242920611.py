#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(A: str, B: str, C: str):
    ss = [A, B, C]
    indices = [0, 0, 0]
    tmp = 0
    while True:
        if indices[tmp] >= len(ss[tmp]):
            ret = chr(ord('A') + tmp)
            break
        nex = ss[tmp][indices[tmp]]
        indices[tmp] += 1
        tmp = ord(nex) - ord('a')
    print(ret)
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
