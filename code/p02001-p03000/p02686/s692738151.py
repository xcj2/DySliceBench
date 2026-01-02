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
    neg_dm = []
    pos_dm = []
    for i in range(n):
        S = input()
        depth = 0
        max_depth = 0
        for c in S:
            if c == '(':
                depth -= 1
            else:
                depth += 1
                max_depth = max(max_depth, depth)
        if depth < 0:
            neg_dm.append([max_depth, depth])
        else:
            pos_dm.append([max_depth, depth])

    neg_dm.sort()
    pos_dm.sort(key = lambda x : [x[1]-x[0], -x[0]])

    # print (neg_dm)
    # print (pos_dm)
    curr_depth = 0
    for m, d in neg_dm:
        if m > -curr_depth:
            print ("No")
            return
        curr_depth += d

    for m, d in pos_dm:
        if m > -curr_depth:
            print ("No")
            return
        curr_depth += d

    if curr_depth == 0:
        print ("Yes")
    else:
        print ("No")


mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
