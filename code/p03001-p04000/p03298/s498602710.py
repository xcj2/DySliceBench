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

from itertools import product

N = I()
S = str(input())

# 右側半分の組の全列挙
d = defaultdict(lambda:defaultdict(int))
A = list(product([0,1],repeat=N))
for a in A:
    x = []
    y = []
    for i in range(N):
        if a[i]:
            x.append(S[N+i])
        else:
            y.append(S[N+i])
    x = ''.join(x)
    y = ''.join(y)
    d[x][y] += 1

# 左側半分で各塗り方を全列挙
# 右側半分の赤，青の値が決まる
ans = 0
for a in A:
    x = []
    y = []
    for i in range(N):
        if a[i]:
            x.append(S[i])
        else:
            y.append(S[i])
    x = ''.join(x[::-1])
    y = ''.join(y[::-1])
    ans += d[x][y]
    
print(ans)