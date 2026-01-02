#!/usr/bin/env python3
import sys

def count(s, t):
    ret = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ret += 1
    return ret


def solve(S: int):
    t1 = []
    t2 = []
    for i in range(len(S)):
        t1.append(str(i % 2))
        t2.append(str((i + 1) % 2))
    t1 = ''.join(t1)
    t2 = ''.join(t2)
    ret = min(count(S, t1), count(S, t2))
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))
    solve(S)

if __name__ == '__main__':
    main()
