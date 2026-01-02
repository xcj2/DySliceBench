import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()
c = list(input())

ans = 0
l = 0
r = N-1
while l <= r:
    flag = False
    for i in range(l,N):
        if c[i] == 'W':
            l = i
            flag = True
            break
    if not flag:
        l = N

    flag = False
    for i in range(r+1)[::-1]:
        if c[i] == 'R':
            r = i
            flag = True
            break
    if not flag:
        r = -1

    if r < l:
        break
    
    c[l] = 'R'
    c[r] = 'W'
    ans += 1

print(ans)