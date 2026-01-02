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
    N, M = MI()
    S, C = [], []
    for i in range(M):
        s, c = MI()
        S.append(s - 1)
        C.append(c)

    ans = [-1] * N

    for i in range(M):
        if ans[S[i]] != -1 and ans[S[i]] != C[i]:
            print(-1)
            exit()

        ans[S[i]] = C[i]

    if ans[0] == 0:
        if N != 1:
            print(-1)
            exit()
        else:
            print(0)
            exit()

    if N == 1 and ans[0] == -1:
        print(0)
        exit()

    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0 if i != 0 else 1
        ans[i] = str(ans[i])

    print("".join(ans))


main()
