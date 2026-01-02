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


h = fetch_int_input()[0]

count = 0
def attack(tmp_h):
    global count
    if tmp_h > 1:
        attack(tmp_h / 2)
        attack(tmp_h / 2)
        count += 1
    else:
        count += 1
        return
import math
while h >= 1:
    h = math.floor(h / 2)
    count += 1

answer = 0
for i in range(count):
    answer += pow(2, i)
print(answer)

