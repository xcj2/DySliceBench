from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))



def solve():
    n, m, q = rl()
    Q = []
    for i in range(q):
        Q.append(rl())

    ways = [[i] for i in range(1, m + 1)]
    for i in range(n - 1):
        new_ways = []
        for way in ways:
            new_way = list(way)
            for j in range(way[-1], m + 1):
                new_ways.append(new_way + [j])
        ways = new_ways

    best = 0
    for way in ways:
        tot = 0
        for a, b, c, d in Q:
            if way[b - 1] - way[a - 1] == c:
                tot += d
        best = max(best, tot)

    print (best)







mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
