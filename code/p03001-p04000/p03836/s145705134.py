#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(sx: int, sy: int, tx: int, ty: int):
    ret = ''
    ret += 'U' * (ty - sy)
    ret += 'R' * (tx - sx)
    ret += 'D' * (ty - sy)
    ret += 'L' * (tx - sx + 1)
    ret += 'U' * (ty - sy + 1)
    ret += 'R' * (tx - sx + 1)
    ret += 'D'
    ret += 'R'
    ret += 'D' * (ty - sy + 1)
    ret += 'L' * (tx - sx + 1)
    ret += 'U'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    sx = int(next(tokens))  # type: int
    sy = int(next(tokens))  # type: int
    tx = int(next(tokens))  # type: int
    ty = int(next(tokens))  # type: int
    solve(sx, sy, tx, ty)

if __name__ == '__main__':
    main()
