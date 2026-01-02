import sys
from itertools import combinations
import math


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
prev_t = 0
prev_x = 0
prev_y = 0
for i in range(N):
    t, x, y = LI()
    if abs(prev_x-x) + abs(prev_y-y) > (t - prev_t) or (abs(prev_x-x) + abs(prev_y-y) + (t - prev_t)) % 2:
        print('No')
        exit()
    prev_t = t
    prev_x = x
    prev_y = y
print('Yes')
