#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int):
    def _convert(cur):
        ret = [''] * N
        for i, pos in enumerate(cur):
            c = chr(ord('a') + i)
            for p in pos:
                ret[p] = c
        ret = ''.join(ret)
        return ret
    def rec(idx, cur):
        if idx == N:
            ret = _convert(cur)
            return [ret]
        ret = []
        for c in cur:
            c.append(idx)
            tmp = rec(idx + 1, cur)
            ret += tmp
            c.pop()
        cur.append([idx])
        ret += rec(idx + 1, cur)
        cur.pop()

        return ret
    ret = rec(0, [])
    for r in ret:
        print(r)
    #print(ret)
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
