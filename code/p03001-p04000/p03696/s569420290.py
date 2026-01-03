#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, S: str):
    pre = 0
    op = 0
    for c in S:
        if c == '(':
            op += 1
        elif c == ')':
            if op > 0:
                op -= 1
            else:
                pre += 1
    ret = (''.join(['(' for _ in range(pre)]) + S + 
           ''.join([')' for _ in range(op)]))
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
