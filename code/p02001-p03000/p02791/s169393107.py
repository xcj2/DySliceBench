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

N = int(fetch_one_line())
nums = fetch_int_input()

min_num = 999999999999999999
count = 0

for num in nums:
    if min_num >= num:
        count += 1
        min_num = num

print(count)

