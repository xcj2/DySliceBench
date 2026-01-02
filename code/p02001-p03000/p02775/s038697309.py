#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(n: str):
    n = n[::-1]
    ret = 0
    carry = 0
    for i, c in enumerate(n):
        t = int(c)
        t += carry
        if t == 5:
            if i < len(n) - 1 and int(n[i + 1]) >= 5:
                ret += 10 - t
                carry = 1
            else:
                ret += t
                carry = 0
        elif t < 5:
            ret += t
            carry = 0
        else:
            ret += 10 - t
            carry = 1
    if carry:
        ret += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = str(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
