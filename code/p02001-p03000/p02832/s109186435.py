from sys import stdin


def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]


def fetch_int_inputs(times):
    return [[int(s) for s in fetch_one_line()] for _ in range(times)]

fetch_one_line()
nums = fetch_int_input()
now_num = 1
remove_num = 0

for n in nums:
    if n == now_num:
        now_num += 1
    else:
        remove_num += 1


if now_num == 1:
    remove_num = -1

print(remove_num)


