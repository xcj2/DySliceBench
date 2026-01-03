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
t = [1 if i == 'o' else 0 for i in s]
def generate(res):
    for i in range(1,n):
        if res[-1]:
            if t[i]:
                if res[-2]:
                    res.append(1)
                else:
                    res.append(0)
            else:
                if res[-2]:
                    res.append(0)
                else:
                    res.append(1)
        else:
            if t[i]:
                if res[-2]:
                    res.append(0)
                else:
                    res.append(1)
            else:
                if res[-2]:
                    res.append(1)
                else:
                    res.append(0)
    return res

def ret(ans):
    res = ["S"]*n
    for i in range(n):
        if ans[i] == 0:
            res[i] = "W"
    return ''.join(res)

ans1 = [1]
ans2 = [1]
ans3 = [1]
ans4 = [1]
if t[0]:
    ans1.append(1)
    ans2.append(0)
    res1 = generate(ans1)
    res2 = generate(ans2)
    if res1[-1] == ans1[0] and ans1[1] == res1[-2]:
        print(ret(res1[:-1]))
        quit()
    elif res2[-1] == ans2[0] and ans2[1] == res2[-2]:
        print(ret(res2[:-1]))
        quit()
else:
    ans3.append(1)
    ans4.append(0)
    res3 = generate(ans3)
    res4 = generate(ans4)
    if res3[-1] == ans3[0] and ans3[1] != res3[-2]:
        print(ret(res3[:-1]))
        quit()
    elif res4[-1] == ans4[0] and ans4[1] != res4[-2]:
        print(ret(res4[:-1])) 
        quit()


ans5 = [0]
ans6 = [0]
ans7 = [0]
ans8 = [0]
if t[0]:
    ans5.append(1)
    ans6.append(0)
    res5 = generate(ans5)
    res6 = generate(ans6)
    if res5[-1] == ans5[0] and ans5[1] != res5[-2]:
        print(ret(res5[:-1]))
        quit()
    elif res6[-1] == ans6[0] and ans6[1] != res6[-2]:
        print(ret(res6[:-1]))
        quit()

else:
    ans7.append(1)
    ans8.append(0)
    res7 = generate(ans7)
    res8 = generate(ans8)
    if res7[-1] == ans7[0] and ans7[1] == res7[-2]:
        print(ret(res7[:-1]))
        quit()
    elif res8[-1] == ans8[0] and ans8[1] == res8[-2]:
        print(ret(res8[:-1]))
        quit()

print(-1)
