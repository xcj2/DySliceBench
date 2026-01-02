#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(s: str, K: int):
    N = len(s)
    for i in range(ord('a'), ord('z')+1):
        c = chr(i)
        l = -1
        subs = []
        while c in s[l+1:]:
            l = s.index(c, l+1)
            for r in range(l+1, min(N+1, l+1+K)):
                subs.append(s[l:r])
        subs = sorted(list(set(subs)))
        if len(subs) > K-1:
            break
        else:
            K -= len(subs)
            continue
    print(subs[K-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(s, K)


if __name__ == '__main__':
    main()
