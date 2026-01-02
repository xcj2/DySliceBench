from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, m = rl()
    roads = dd(set)
    heights = rl()
    for i in range(m):
        u, v = rl()
        roads[u].add(v)
        roads[v].add(u)

    good = 0
    for i in range(1, n + 1):
        for nbr in roads[i]:
            if heights[nbr - 1] >= heights[i - 1]:
                break
        else:
            good += 1

    print (good)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
