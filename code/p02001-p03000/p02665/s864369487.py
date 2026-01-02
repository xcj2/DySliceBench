#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    cur = 1
    ret = 0
    t = []
    for i in range(N):
        v = A[i]
        if v >= cur:
            print(-1)
            return
        t.append(cur)
        ret += cur
        #print(i, cur, ret)
        cur = (cur - v) * 2
    if A[-1] > cur:
        print(-1)
        return
    ret += A[-1]
    #print(ret)

    mx = A[-1]
    for i in range(1, N)[::-1]:
        tmp = min(mx + A[i], 2 ** i)
        if t[i] > tmp:
            ret -= t[i] - tmp
        #ret += tmp
        mx = min(tmp, 2 ** (i - 1))
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 0 + 1)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
