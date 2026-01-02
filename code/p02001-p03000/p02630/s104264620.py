from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n = ri()
    A = rl()
    counts = dd(int)
    total  = 0
    for a in A:
        total += a
        counts[a] += 1

    for _ in range(ri()):
        x, y = rl()
        rem = counts[x]
        total += (y - x) * rem
        counts[x] = 0
        counts[y] += rem
        print (total)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
