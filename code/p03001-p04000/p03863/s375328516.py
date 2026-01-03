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

# 2文字の繰り返しで負け
# これはs[0]=s[-1]なら奇数文字，s[0]!=s[-1]なら偶数文字

s = str(input())

if s[0] == s[-1]:
    if len(s)%2:
        print('Second')
    else:
        print('First')
else:
    if len(s)%2:
        print('First')
    else:
        print('Second')