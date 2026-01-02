#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    for i in range(N):
        A[i] -= i + 1
    A.sort()
    tmp = A[0]
    for i in range(N):
        A[i] -= tmp
    l = -1
    r = N
    cur = sum(A)
    #print(A)
    while r - l > 1:
        m = (l + r) // 2
        val = A[m]
        tmp = 0
        for a in A:
            tmp += abs(a - val)
        if tmp <= cur:
            l = m
            cur = tmp
        else:
            r = m
    val = A[l]
    ret = 0
    for a in A:
        ret += abs(a - val)

    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
