#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, S: int):
    cur = N
    ret = []
    while cur - M > 0:
        found = False
        t = -1
        for i in range(M, 0, -1):
            if S[cur - i] == '0':
                t = i
                break
        if t > 0:
            cur -= t
            ret.append(t)
        else:
            print(-1)
            return
    ret.append(cur)
    ret.reverse()
    ret = ' '.join([str(r) for r in ret])
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: int
    solve(N, M, S)

if __name__ == '__main__':
    main()
