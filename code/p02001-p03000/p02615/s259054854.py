#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    A.sort(reverse=True)
    ret = 0
    #tmp = [A[0], A[1]]
    #for i in range(2, N):
    #    ret

    ret += A[0]
    cnt = 1
    i = 1
    while cnt < N - 1:
        #print(cnt, i, A[i])
        ret += A[i]
        cnt += 1
        if cnt % 2 == 1:
            i += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
