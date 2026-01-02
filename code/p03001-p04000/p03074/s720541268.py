#!/usr/bin/env python3
import sys
import itertools
INF = float("inf")


def solve(N: int, K: int, S: str):
    s = []
    buf = 0
    mode = S[0]
    for c in S:
        if c == mode:
            buf += 1
        else:
            s.append(buf)
            buf = 1
            mode = c
    s.append(buf)

    # 1始まり1終わり
    if S[0] == "0":
        s = [0]+s
    if S[-1] == "0":
        s = s+[0]
    # print(s)

    tot = [0]+list(itertools.accumulate(s))
    w = 2*K+1
    hint = [tot[i+w]-tot[i] for i in range(0, len(tot)-w, 2)]
    if len(hint) == 0:
        print(len(S))
    else:
        print(max(hint))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = str(next(tokens))  # type: int
    solve(N, K, S)


if __name__ == '__main__':
    main()
