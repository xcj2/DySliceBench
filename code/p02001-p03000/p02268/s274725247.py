import sys
from collections import deque
from itertools import *

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        center = int((left + right) / 2)
        if list[center] == target:
            return center
        elif list[center] < target:
            left = center + 1
        elif list[center] > target:
            right = center - 1
    return None

n = I()
s = LI()
q = I()
t = LI()
ans = 0
for t_t in t:
    if binary_search(s,t_t) is not None:
        ans += 1
print(ans)
