from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor

import heapq
import itertools
import operator


inf = float('inf')


def get_int():
    return int(input())


def get_str():
    return input().strip()


def get_list_of_int():
    return [int(i) for i in input().split()]


def get_char_list():
    return list(input().strip())


# inputs
A, B, Q = 0, 0, 0
S = []
T = []
X = []


def set_inputs():
    global A, B, Q, S, T, X
    A, B, Q = get_list_of_int()
    for _ in range(A):
        S.append(get_int())
    for _ in range(B):
        T.append(get_int())
    for _ in range(Q):
        X.append(get_int())


def main():
    set_inputs()

    for i in range(Q):
        nsi = bisect_left(S, X[i])
        if nsi == 0:
            ns = inf
        else:
            ns = X[i] - S[nsi-1]
        psi = bisect_left(S, X[i])
        if psi == A:
            ps = inf
        else:
            ps = S[nsi] - X[i]
        nti = bisect_left(T, X[i])
        if nti == 0:
            nt = inf
        else:
            nt = X[i] - T[nti-1]
        pti = bisect_left(T, X[i])
        if pti == B:
            pt = inf
        else:
            pt = T[nti] - X[i]
        print(min(max(ns, nt), max(ps, pt), ns * 2 + pt, ns + pt * 2, nt * 2 + ps, nt + ps * 2))


if __name__ == '__main__':
    main()
