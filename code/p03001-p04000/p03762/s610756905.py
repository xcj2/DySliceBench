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

# 小区間ごとに個数を数えて足し合わせると，
# summationの中身がxとyについて独立になっている

n,m = LI()
x = LI()
y = LI()

xsum = 0
for i in range(n-1):
    xsum += (i+1)*(n-i-1)*(x[i+1]-x[i])
    xsum %= mod

ysum = 0
for j in range(m-1):
    ysum += (j+1)*(m-j-1)*(y[j+1]-y[j])
    ysum %= mod

print(xsum*ysum%mod)