#!/usr/bin/env python3
import sys
# sys.setrecursionlimit(10000000)
# INF = 1<<32s


def solve(N: int, S: str):
    ans = 0
    for i in range(1000):
        si = format(i, '03')

        idx = 0
        for j in range(len(S)):
            if idx >= len(si):
                break
            elif si[idx] == S[j]:
                idx += 1

        if idx == len(si):
            ans += 1

    print(ans)
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = str(next(tokens))  # type: int
    solve(N, S)

if __name__ == '__main__':
    main()
