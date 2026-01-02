import sys
from collections import deque
from itertools import *


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


n = I()
s = S()

ans = 0
for i in range(1000):
    t = str(i).zfill(3)
    t_index = 0
    for s_index in range(n):
        if s[s_index] == t[t_index]:
            t_index += 1
            if t_index == 3:
                break
    if t_index == 3:
        ans += 1
print(ans)
