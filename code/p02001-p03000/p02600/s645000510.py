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

if 400 <= X <= 599:
    print('8')
elif 600 <= X <= 799:
    print('7')
elif 800 <= X <= 999:
    print('6')
elif 1000 <= X <= 1199:
    print('5')
elif 1200 <= X <= 1399:
    print('4')
elif 1400 <= X <= 1599:
    print('3')
elif 1600 <= X <= 1799:
    print('2')
elif 1800 <= X <= 1999:
    print('1')
else:
    pass