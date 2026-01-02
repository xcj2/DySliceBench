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

K = I()

d = defaultdict(int)
digit = 1
val = 7%K
while True:
    if val == 0:
        print(digit)
        exit()
    else:
        if d[val]:
            print(-1)
            exit()
        d[val] += 1
        digit += 1
        val = 10*val+7
        val %= K