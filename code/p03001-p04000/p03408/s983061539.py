#■標準入力ショートカット

from collections import defaultdict


def get_next_int():
    return int(float(input()))


def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_str():
    return input()


def get_next_strs(delim=" "):
    return tuple(input().split(delim))


def get_next_by_types(*value_types, delim=" "):
    return tuple([t(x) for t, x in zip(value_types, input().split(delim))])


def solve():
    N = get_next_int()
    ans = defaultdict(int)
    for i in range(N):
        key = input()
        ans[key] += 1
    M = get_next_int()
    for i in range(M):
        key = input()
        ans[key] -= 1
    max_val = max(ans.values())
    value = 0 if max_val < 0 else max_val
    print(value)


solve()