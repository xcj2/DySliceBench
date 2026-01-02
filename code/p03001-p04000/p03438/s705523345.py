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
B = LI()

x = 0
y = 0
for i in range(N):
    a = A[i]
    b = B[i]
    if a < b:
        if (b-a)%2 == 0:
            x += (b-a)//2
        else:
            x += (b-a)//2 + 1
            y += 1
    else:
        y += a-b

if x < y:
    print('No')
    exit()
count = 2*x-y

if count == sum(B)-sum(A) and count >= 0:
    print('Yes')
else:
    print('No')