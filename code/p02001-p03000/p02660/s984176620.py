#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int):
    ps = []
    i = 2
    ret = 0
    def _is_p(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    ret = 0
    while i * i <= N:
        #if not _is_p(i):
        #    continue
        t = 0
        while N % i == 0:
            t += 1
            N //= i
        if t > 0:
            #print(i, t, N)
            j = 1
            s = 0
            while s + j <= t:
                s += j
                ret += 1
                j += 1
        i += 1

    if _is_p(N):
        ret += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
