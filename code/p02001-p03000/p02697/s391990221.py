#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int):
    if N % 2 == 1:
        s = N // 2
        for i in range(M):
            v = i * 2 + 1
            print(s, s + v)
            #print(s, s + v, v, N - v)
            s -= 1
    else:
        s = N // 2
        cnt = 0
        used = set()
        for i in range(M // 2 + 1):
            v = i * 2 + 1
            if v == N // 2 or v in used:
                continue
            print(s, s + v)
            #print(s, s + v, v, N - v)
            s -= 1
            cnt += 1
            used.add(v)
            used.add(N - v)
        s = 1
        for i in range(M - cnt):
            v = N - s - s
            print(s, N - s)
            #print(s, N - s, v, N - v)
            s += 1
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
