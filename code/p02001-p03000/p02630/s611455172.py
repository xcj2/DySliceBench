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

N = I()
A = LI()
Q = I()
B,C = LIR(Q,2)

ans = []
d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

sum_ = sum(A)
for i in range(Q):
    num = d[B[i]]
    sum_ = sum_+num*(C[i]-B[i])
    ans.append(sum_)
    d[B[i]] -= num
    d[C[i]] += num

for a in ans:
    print(a)