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

N,X,Y = LI()

X -= 1
Y -= 1
d = defaultdict(int)
for i in range(N):
    for j in range(i+1,N):
        val = min(abs(X-i)+1+abs(Y-j), abs(X-j)+1+abs(Y-i), abs(i-j))
        d[val] += 1

for i in range(1,N):
    print(d[i])