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


a, b = fetch_one_line().split(" ")
a_n, b_n = [int(i) for i in fetch_one_line().split(" ")]
remove_str = fetch_one_line()

if a == remove_str:
    a_n -= 1

else:
    b_n -= 1

print(a_n, b_n)


