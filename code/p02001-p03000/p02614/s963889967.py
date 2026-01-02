from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
from itertools import combinations as comb

def subsets(L):
    for i in range(len(L) + 1):
        for c in comb(L, i):
            yield c


def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    h, w, k = rl()
    grid = []
    for i in range(h):
        grid.append(input())


    def test(rows, cols):
        blacks = 0
        for i in range(h):
            if i in rows:
                continue
            for j in range(w):
                if j in cols:
                    continue
                if grid[i][j] == "#":
                    blacks += 1
        return blacks

    ans = 0
    for rowset in subsets(range(h)):
        for colset in subsets(range(w)):
            if test(rowset, colset) == k:
                ans += 1

    print (ans)





mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
