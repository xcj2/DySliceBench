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

N,Q = LI()

a = [N-1]*N  # 各行の白石の最左
b = [N-1]*N  # 各列の白石の最上

a[-1] = 0
b[-1] = 0

x1 = N-1  # 枠の縦位置
x2 = N-1  # 枠の横位置

ans = (N-2)**2
for i in range(Q):
    j,k = LI()
    k -= 1
    if j == 1:
        if k > x2:
            ans -= (b[k]-1)
        else:
            for n in range(k+1,x2):
                b[n] = x1
            ans -= max(0,(x1-1))
            x2 = k
    else:
        if k > x1:
            ans -= (a[k]-1)
        else:
            for n in range(k+1,x1):
                a[n] = x2
            ans -= max(0,(x2-1))
            x1 = k

print(ans)