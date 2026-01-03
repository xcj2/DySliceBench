#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, S: "List[str]"):
    ret = 1
    status = 0
    i = 0
    while i < N:
        #print(i, status, ret)
        if status == 1:
            ret *= 2
        if S[0][i] == S[1][i]:
            if status == 0:
                ret *= 3
            status = 1
        else:
            if status == 0:
                ret *= 3 * 2
            elif status == 2:
                ret *= 3
            status = 2
            i += 1
        i += 1
        ret %= MOD
    ret %= MOD
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(2) ]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
