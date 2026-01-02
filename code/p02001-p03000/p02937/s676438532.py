#!/usr/bin/env python3
import sys, bisect
sys.setrecursionlimit(300000)


def solve(s: str, t: str):
    N = 26
    pos = [[] for _ in range(N)]
    for i, c in enumerate(s):
        pos[ord(c) - ord('a')].append(i)

    tmp = 0
    num = 0
    for C in t:
        c = ord(C) - ord('a')
        le = len(pos[c])
        if le < 1:
            print(-1)
            return
        idx = bisect.bisect_left(pos[c], tmp)
        #print(pos[c], C, idx)
        if idx < le:
            tmp = pos[c][idx] + 1
        else:
            idx = bisect.bisect_left(pos[c], 0)
            tmp = pos[c][idx] + 1
            num += 1
        #print(C, num, tmp)
    ret = num * len(s) + tmp
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)

if __name__ == '__main__':
    main()
