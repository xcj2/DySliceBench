#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, A: "List[int]"):
    #while True:
    for _ in range(K):
        inc = [0] * N
        dec = [0] * N
        for i in range(N):
            s = max(0, i - A[i])
            e = min(N - 1, i + A[i])
            inc[s] += 1
            dec[e] += 1
        nexts = []
        cur = 0
        found = False
        for i in range(N):
            cur += inc[i]
            if cur < N:
                found = True
            nexts.append(cur)
            cur -= dec[i]
        A = nexts
        if not found:
            break
    print(*A, sep=' ')
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
