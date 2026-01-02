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


N, M = fetch_int_input()
nums = fetch_int_input()

sums = [0]
for idx, num in enumerate(nums):
    sums.append(num + sums[idx])
sums = sums[1:]

sums = [s % M for s in sums]

remains = {}

for s in sums:
    if s in remains:
        remains[s] += 1
    else:
        remains[s] = 1

answer = 0
for v in remains.values():
    answer += int(v * (v - 1) / 2)

if 0 in remains:
    answer += remains[0]


print(answer)
