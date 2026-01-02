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

# F2上で基底集合Aにxを追加する
# ex: [[1,0,0],[0,1,0]] + [1,1,1] -> [[1,0,0],[0,1,0],[0,0,1]]
# 各要素は十進数で表記．上の例だと A=[4,2], x=7 -> A=[4,2,1]
def F2_update_basis(A,x):
    for a in A:
        x = min(x,x^a)
    if x:
        A.append(x)
    return A

T = I()
ans = []
for i in range(T):
    N = I()
    A = LI()
    S = list(input())
    d = []
    flag = False
    for j in range(N)[::-1]:
        if S[j] == '0':
            d = F2_update_basis(d,A[j])
        else:
            num = len(d)
            d = F2_update_basis(d,A[j])
            if len(d) != num:
                flag = True
                ans.append(1)
                break
    if not flag:
        ans.append(0)

for a in ans:
    print(a)