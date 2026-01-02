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

# 高橋君のスコア：a*b(a<b)とする
# 1~a-1 は b+a-1~b+1 と組み合わせればok
# a は b-1 と組み合わせればok
# [a+1,b-2]*2 から何ペアできるか二分探索

Q = I()
A,B = LIR(Q,2)

for i in range(Q):
    a,b = min(A[i],B[i]), max(A[i],B[i])
    ab = a*b
    if b-a <= 1:
        print(2*(a-1))
    else:
        ok = 0
        ng = b-a-1
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if mid%2 == 0:
                max_val = (a+mid//2)*(a+mid//2+1)
            else:
                max_val = (a+(mid+1)//2)**2
            if max_val < ab:
                ok = mid
            else:
                ng = mid
        print(2*(a-1)+1+ok)