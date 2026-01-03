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

# 直前要素との差から，自分スタートが何回かわかる
# その和が全試行回数と一致すれば可能

N = I()
A = LI()

red_once = (N+1)*N//2
s = sum(A)

if s%red_once != 0:
    print('NO')
else:
    num = s//red_once
    t = [0]*N
    for i in range(N):
        d,m = divmod(num-A[i]+A[i-1],N)
        if m != 0 or d < 0:
            print('NO')
            exit()
        else:
            t[i] = d
    if sum(t) == num:
        print('YES')
    else:
        print('NO')