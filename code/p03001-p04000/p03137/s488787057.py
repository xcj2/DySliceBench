import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def gcd_multi(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    ret = gcd(nums.pop(), nums.pop())
    while len(nums) > 0:
        ret = gcd(ret, nums.pop())
    return ret


def solve(inputs):
    [N, M] = string_to_int(inputs[0])
    targets = string_to_int(inputs[1])

    if N >= M:
        return 0

    targets.sort()
    diffs = []
    for i in range(0, len(targets)-1):
        diffs.append((i, targets[i+1] - targets[i]))
    diffs.sort(key=lambda x: x[1])

    # separate groups
    separaters = []
    for _ in range(0, N-1):
        separaters.append(diffs.pop()[0])
    separaters.sort()

    groups = []
    prev_sep = -1
    for i, s in enumerate(separaters):
        groups.append(targets[prev_sep+1:s+1])
        prev_sep = s
    groups.append(targets[prev_sep+1:])

    counts = 0
    for g in groups:
        counts += g[-1] - g[0]

    return counts


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
