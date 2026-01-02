#! /usr/bin/env python
# -*- coding: utf-8 -*-

sN = []
sQ = []
dQ = []
Q = 0
N = 0


def gor(pos):
    for i in range(Q):
        if sN[pos] == sQ[i]:
            if dQ[i] == 'R':
                pos = pos + 1
            else:
                pos = pos - 1

            if pos < 0:
                return False
            if pos > N - 1:
                return True

    return False


def getr():
    l = 0
    r = N - 1
    res = N
    while r >= l:
        mid = (l + r) // 2
        if gor(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res


def gol(pos):
    for i in range(Q):
        if sN[pos] == sQ[i]:
            if dQ[i] == 'L':
                pos = pos - 1
            else:
                pos = pos + 1

            if pos > N - 1:
                return False
            if pos < 0:
                return True

    return False


def getl():
    l = 0
    r = N - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if gol(mid):
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res


if __name__ == '__main__':
    N, Q = map(int, input().split())  # N, Q for number

    sN = input()  # squares

    for i in range(0, Q):
        t, d = input().split()
        sQ.append(t)
        dQ.append(d)
        #sQ.append({'t': t, 'd': d})

    removed_l = getl() + 1
    removed_r = N - getr()

    print(N - removed_l - removed_r)
