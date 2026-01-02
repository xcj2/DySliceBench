from collections import defaultdict as dd
from collections import deque
from itertools import combinations as combination
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def subset(A):
    for l in range(len(A) + 1):
        for comb in combination(A, l):
            yield comb

def solve():
    n, m, x = rl()
    C = []
    A = []
    for i in range(n):
        line = rl()
        C.append(line[0])
        A.append(line[1:])

    min_cost = 10**20
    for sub in subset(range(n)):
        skills = [0] * m
        cost = 0
        for s in sub:
            for i in range(m):
                skills[i] += A[s][i]
            cost += C[s]

        for skill in skills:
            if skill < x:
                break
        else:
            min_cost = min(min_cost, cost)

    if min_cost == 10**20:
        print (-1)
    else:
        print (min_cost)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
