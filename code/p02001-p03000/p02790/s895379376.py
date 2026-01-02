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

a, b = fetch_int_input()

strs = []
strs.append("".join([str(a) for _ in range(b)]))
strs.append("".join([str(b) for _ in range(a)]))

print(sorted(strs)[0])
