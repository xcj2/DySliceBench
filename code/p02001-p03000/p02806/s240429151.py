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
s_t = fetch_inputs(N)
X = fetch_one_line()

flag = False
sum_time = 0
for tmp in s_t:
    s, t = tmp.split(" ")
    if not flag and s == X:
        flag = True
        continue

    t = int(t)
    if flag:
        sum_time += t

print(sum_time)

