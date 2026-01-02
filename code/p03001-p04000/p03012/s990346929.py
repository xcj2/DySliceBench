from sys import stdin


def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]


def fetch_int_inputs(times):
    return [[int(s) for s in fetch_one_line()] for _ in range(times)]


def fetch_ints_inputs(times):
    return [fetch_int_input() for _ in range(times)]

fetch_one_line()
nums = fetch_int_input()
min_dist = 9999999999999999999
min_t = -1
for i in range(len(nums)):
    dist = abs(sum(nums[:i]) - sum(nums[i:]))
    if min_dist > dist:
        min_dist = dist
        min_t = i

print(min_dist)
