#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N, M, Q = MI()
    targets = [[] for i in range(Q)]
    for i in range(Q):
        target = LI()
        targets[i] = target
    ans = 0
    for i in range(1, 2**(M+N)):
        i_str = format(i, f"0{M+N-1}b")
        A = []
        tmp = 1
        for k in range(len(i_str)):
            if i_str[k] == "1":
                tmp += 1
            else:
                A.append(tmp)
        if len(A) != N:
            continue
        score = 0
        for query in targets:
            a, b, c, d = query
            if A[b-1] - A[a-1] == c:
                score += d
        ans = max(ans, score)

    print(ans)


main()
