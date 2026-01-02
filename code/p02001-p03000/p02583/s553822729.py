#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, L: "List[int]"):
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                s = L[i] + L[j] + L[k]
                m = max(L[i], L[j], L[k])
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and m < s - m:
                    ret += 1
                    #print(i, j, k)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L)

if __name__ == '__main__':
    main()
