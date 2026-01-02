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

from decimal import getcontext, Decimal

def count5(n):
    count = 0
    while n%5 == 0:
        count += 1
        n //= 5
    return count

def count2(n):
    count = 0
    while n%2 == 0:
        count += 1
        n //= 2
    return count

N = I()
A = []
for i in range(N):
    A.append(int(10**9*Decimal(input())))

counter = [[0]*30 for _ in range(50)]
for i in range(N):
    c2 = count2(A[i])
    c5 = count5(A[i])
    counter[c2][c5] += 1

same = 0
diff = 0
for i in range(50):
    for j in range(30):
        if counter[i][j]:
            for p in range(18-i,50):
                for q in range(18-j,30):
                    if i != p or j != q:
                        diff += counter[i][j]*counter[p][q]
                    else:
                        same += counter[i][j]*(counter[p][q]-1)//2

print(diff//2+same)