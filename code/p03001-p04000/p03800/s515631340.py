#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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

n = I()
s = input()
check1 = [None] * n
check1[0] = 'S'
check1[1] = 'S'
check2 = [None] * n
check2[0] = 'S'
check2[1] = 'W'
check3 = [None] * n
check3[0] = 'W'
check3[1] = 'S'
check4 = [None] * n
check4[0] = 'W'
check4[1] = 'W'
def check(lst):
    for i in range(1,n):
        if lst[i] == 'S':
            if s[i] == 'o':
                if i + 1 == n:
                    if lst[0] != lst[i-1]:
                        return False, lst
                else:
                    lst[i+1] = lst[i-1]
            else:
                if i + 1 == n:
                    if lst[0] == lst[i-1]:
                        return False, lst
                else:
                    if lst[i-1] == 'S':
                        lst[i+1] = 'W'
                    else:
                        lst[i+1] = 'S'
        else:
            if s[i] == 'o':
                if i + 1 == n:
                    if lst[0] == lst[i-1]:
                        return False, lst
                else:
                    if lst[i-1] == 'S':
                        lst[i+1] = 'W'
                    else:
                        lst[i+1] = 'S'
            else:
                if i + 1 == n:
                    if lst[0] != lst[i-1]:
                        return False, lst
                else:
                    lst[i+1] = lst[i-1]
    else:
        if s[0] == 'o' and lst[0] == 'S':
            if lst[-1] != lst[1]:
                return False, lst
        elif s[0] == 'o' and lst[0] == 'W':
            if lst[-1] == lst[1]:
                return False, lst
        elif s[0] == 'x' and lst[0] == 'S':
            if lst[-1] == lst[1]:
                return False, lst
        elif s[0] == 'x' and lst[0] == 'W':
            if lst[-1] != lst[1]:
                return False, lst
        return True, lst

f1, check1 = check(check1)
if f1:
    print(''.join(check1))
    quit()
f2, check2 = check(check2)
if f2:
    print(''.join(check2))
    quit()
f3, check3 = check(check3)
if f3:
    print(''.join(check3))
    quit()
f4, check4 = check(check4)
if f4:
    print(''.join(check4))
    quit()
print(-1)
            