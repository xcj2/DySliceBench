#!/usr/bin/env python3
import sys


def solve(H: int, W: int, S: "List[str]"):
    ret = []
    for x, R in enumerate(S):
        r = ''
        for y, c in enumerate(R):
            if c == '.':
                tmp = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < H and 0 <= y + j < W and S[x + i][y + j] == '#':
                            tmp += 1
                r += str(tmp)
            else:
                r += c
        ret.append(r)

    for r in ret:
        print(r)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
