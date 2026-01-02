import numpy as np


def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def main():
    N = ii()
    S = input()
    e = 0
    for v in S:
        if v == 'E': e += 1

    min_n_turn = N
    ec = 0
    for i in range(N):
        ew = (N - i - 1) - (e - ec - int(S[i] == 'E'))
        n_turn = N - 1 - ec - ew
        if S[i] == 'E':
            ec += 1
        # print(ec, ew, n_turn)
        min_n_turn = min(min_n_turn, n_turn)

    return min_n_turn

if __name__ == '__main__':
    print(main())