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

S = str(input())

count = 0
max_count = 0
for i in range(3):
    if S[i] == 'R':
        if i >= 1 and S[i-1] == 'R':
            count += 1
        else:
            count = 1
    max_count = max(count,max_count)

print(max_count)