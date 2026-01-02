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


N, hit_point = fetch_int_input()
swords = fetch_ints_inputs(N)
SLASH, THROW = 0, 1

max_slash_id, max_slash = -1, -1

for idx, sword in enumerate(swords):
    if max_slash <= sword[SLASH]:
        if max_slash == sword[SLASH] and sword[THROW] < swords[max_slash_id][THROW]:
            continue

        max_slash = sword[SLASH]
        max_slash_id = idx


max_slash_throw = swords[max_slash_id][THROW]
# del swords[max_slash_id]
large_throw_swords = list(filter(lambda x: x[THROW] > max_slash, swords[:]))
large_throw_swords.sort(key=lambda x: x[1], reverse=True)

count = 0
is_clear = False

for s in large_throw_swords:

    # if max_slash_throw >= H:
    #    count += 1
    #    H -= max_slash_throw
    #    break

    hit_point -= s[THROW]
    count += 1
    if hit_point <= 0:
        break

import math
if hit_point > 0:
    count += math.ceil(hit_point / max_slash)

print(count)

