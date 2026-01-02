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
S, T = "", ""


def set_inputs():
    global S, T
    S = get_str()
    T = get_str()
    return


def main():
    set_inputs()
    dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    i = len(S)
    j = len(T)
    ret = ""

    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ret += S[i-1]
            i -= 1
            j -= 1
    print(''.join(reversed(ret)))


if __name__ == '__main__':
    main()
