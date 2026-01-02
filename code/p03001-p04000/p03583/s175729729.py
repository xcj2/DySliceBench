import sys
import math
from collections import defaultdict

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

flag = False
for h in range(1,3501):
    for n in range(h,3501):
        a = 4*h*n-N*n-N*h
        b = N*h*n
        if a > 0 and b%a == 0:
            w = b//a
            flag = True
            break
    if flag:
        break

print(h,n,w)