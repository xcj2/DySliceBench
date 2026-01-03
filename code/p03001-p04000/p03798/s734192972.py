#!/usr/bin/env python3
#ABC55 D

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

def check(t):
    for i in range(n):
        if t[i] == 'S':
            if s[i] == 'o':
                if i == n-1:
                    if t[i-1] != t[0]:
                        return False
                        break
                else:
                    if t[i-1] != t[i+1]:
                        return False
                        break
            else:
                if i == n-1:
                    if t[i-1] == t[0]:
                        return False
                        break
                else:
                    if t[i-1] == t[i+1]:
                        return False
                        break
        if t[i] == 'W':
            if s[i] == 'o':
                if i == n-1:
                    if t[i-1] == t[0]:
                        return False
                        break
                else:
                    if t[i-1] == t[i+1]:
                        return False
                        break
            else:
                if i == n-1:
                    if t[i-1] != t[0]:
                        return False
                        break
                else:
                    if t[i-1] != t[i+1]:
                        return False
    return True

n = I()
s = input()
tmp = ['SS','SW','WS','WW']
for x in tmp:
    for i in range(1,n-1):
        if s[i] == 'o':
            if x[-1] == 'S':
                if x[-2] == 'W':
                    x += 'W'
                else:
                    x += 'S'
            else:
                if x[-2] == 'W':
                    x += 'S'
                else:
                    x += 'W'
        else:
            if x[-1] == 'S':
                if x[-2] == 'W':
                    x += 'S'
                else:
                    x += 'W'
            else:
                if x[-2] == 'W':
                    x += 'W'
                else:
                    x += 'S'
    if check(x):
        print(x)
        quit()
print(-1)
