#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]"):
    a, b = [0], [0]
    for v in A:
        a.append(a[-1] + v)
    for v in B:
        b.append(b[-1] + v)

    j = M
    ret = 0
    #print(a)
    #print(b)
    for i, v in enumerate(a):
        while j > 0 and v + b[j] > K:
            j -= 1
        if v + b[j] <= K:
            #print(i, v, j, b[j])
            ret = max(ret, i + j)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, K, A, B)

if __name__ == '__main__':
    main()
