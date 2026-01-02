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

# 掃き出し法
# ex: [[1,1,0],[1,0,1],[1,1,1]] -> [[1,1,0],[0,1,1],[0,0,1]]
# 行ごとの二進数値で入力する．上の例だと A = [6,5,7] -> g = [6,3,1]
def F2_row_reduction(A):
    n = len(A)
    g = A[:]
    rank = 0
    max_digit = len(format(max(A),'b'))
    for col in range(max_digit)[::-1]:
        pivot = -1
        for row in range(rank,n):
            if g[row]>>col & 1:
                pivot = row
                break
        if pivot == -1: 
            continue
        g[pivot],g[rank] = g[rank],g[pivot]
        for row in range(rank+1,n):
            if g[row]>>col & 1:
                g[row] ^= g[rank]
        rank += 1
    return g

T = I()
ans = []
for i in range(T):
    N = I()
    A = LI()
    S = list(input())
    d = []
    flag = False
    for j in range(N)[::-1]:
        rank = 0
        if S[j] == '0':
            d.append(A[j])
            d = F2_row_reduction(d)
            if d[-1] == 0:
                d.pop()
            else:
                rank += 1
        else:
            d.append(A[j])
            d = F2_row_reduction(d)
            if d[-1] == 0:
                d.pop()
            else:
                flag = True
                ans.append(1)
                break
    if not flag:
        ans.append(0)

for a in ans:
    print(a)