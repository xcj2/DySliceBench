#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32
a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def solve(N: int, S: str):
    al = a+a
    ans = []
    for i in range(len(S)):
        ans += al[al.index(S[i])+N]

    print(''.join(ans))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()