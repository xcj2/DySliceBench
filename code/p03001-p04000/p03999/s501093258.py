#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(S: str):
    eqs = [S[0]]
    for i in range(1, len(S)):
        c = S[i]
        nex = []
        for eq in eqs:
            nex.append(eq + '+' + c)
            nex.append(eq + c)
        eqs = nex
    #print(eqs)
    ret = 0
    for eq in eqs:
        nums = eq.split('+')
        for n in nums:
            ret += int(n)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()
