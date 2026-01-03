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
S = list(input())

c = 0
now = 0
left = 0
right = 0
for i in range(N):
    if S[i] == '(':
        now -= 1
        left += 1
    else:
        now += 1
        right += 1
    if c < now:
        c = now

S = ['(']*c + S + [')']*(left+c-right)
print(''.join(S))