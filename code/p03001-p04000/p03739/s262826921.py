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

n = I()
a = LI()

def calc(flag):
    ans = 0
    now = 0
    for i in range(n):
        now += a[i]
        if flag == '+':
            if now <= 0:
                ans += 1-now
                now = 1
            flag = '-'
        else:
            if now >= 0:
                ans += now+1
                now = -1
            flag = '+'
    return ans

print(min(calc('+'),calc('-')))