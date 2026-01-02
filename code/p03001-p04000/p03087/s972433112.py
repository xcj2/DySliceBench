# coding: utf-8
import sys
import itertools


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


N, Q = lr()
S = sr()

ac = [0] * (N - 1)
for i, x in enumerate(zip(S[:], S[1:])):
    if x[0] == 'A' and x[1] == 'C':
        ac[i] = 1

cum = list(itertools.accumulate(ac))
ans_list = []
for _ in range(Q):
    l, r = lr()
    if (l - 2 < 0):
        result = cum[r - 2]
    else:
        result = cum[r - 2] - cum[l - 2]
    ans_list.append(result)
[print(ans) for ans in ans_list]
