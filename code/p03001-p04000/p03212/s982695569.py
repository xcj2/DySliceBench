
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n = list(map(lambda c: ord(c) - ord('0'), input()))



def solve(pos, leading_zero, is_small, i3, i5, i7):

    # print(pos, is_small, i3, i5, i7)

    if pos == len(n):
        if i3 and i5 and i7:
            return 1
        return 0

    res = 0

    for d in [0,3,5,7]:
        if leading_zero == False and d == 0:
            continue
        if not is_small and d > n[pos]:
            continue
        new_is_small = True
        if d == n[pos] and not is_small: new_is_small = False
        new_leading_zero = False
        if leading_zero and d == 0:
            new_leading_zero = True
        res += solve(pos + 1, new_leading_zero, new_is_small,
                     i3 or (d == 3), i5 or (d == 5), i7 or (d == 7))

    return res


print(solve(0, True, False, False, False, False))
