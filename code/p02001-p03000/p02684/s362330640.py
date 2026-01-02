from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, k = rl()
    A = rl()
    # leaps = [A]
    # leap_size = 2
    # while leap_size <= k:
        # new_leap = []
        # for i in range(n):
    curr = 1
    seen = {1:0}

    for i in range(1, k + 1):
        curr = A[curr - 1]
        if i == k:
            print (curr)
            return
        elif curr in seen:
            break
        seen[curr] = i

    cycle_len = i - seen[curr]
    # print (cycle_len)

    while 1:
        if i % cycle_len == k % cycle_len:
            print (curr)
            return
        i += 1
        curr = A[curr - 1]






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
