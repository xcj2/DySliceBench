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

X = I()

count = 1
eps = 10**(-6)
now = [0,1]
while True:
    count += 1
    now[0] -= math.sin(math.radians((count-1)*X))
    now[1] += math.cos(math.radians((count-1)*X))
    if abs(now[0]) < eps and abs(now[1]) < eps:
        print(count)
        exit()