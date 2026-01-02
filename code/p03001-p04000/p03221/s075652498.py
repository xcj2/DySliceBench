from sys import stdin
import bisect

def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]


def fetch_int_inputs(times):
    return [fetch_int_input() for _ in range(times)]


PREF, YEAR = 0, 1

N, M = fetch_int_input()
data = fetch_int_inputs(M)

pre_save = [[] for _ in range(N)]
for d in data:
    pre_save[d[PREF] - 1].append(d[YEAR])

for p in pre_save:
    p.sort()


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


for d in data:
    left = str(d[PREF]).zfill(6)
    right = str(index(pre_save[d[PREF] - 1], d[YEAR]) + 1).zfill(6)
    print(left+right)

