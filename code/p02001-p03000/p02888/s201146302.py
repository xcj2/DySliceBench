#!/usr/bin/env python3
import sys, bisect
sys.setrecursionlimit(300000)


def solve(N: int, L: "List[int]"):
    ret = 0
    L.sort()
    for i in range(N):
        for j in range(i + 1, N):
            mx = L[i] + L[j] - 1
            r = bisect.bisect_right(L, mx)
            cnt = max(0, r - j - 1)
            ret += cnt
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
