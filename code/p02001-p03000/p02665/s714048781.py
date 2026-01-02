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

def ceil(a,b):
    return a//b + int(a%b != 0)

N = I()
A = LI()

mau = [0]*(N+1)
miu = [0]*(N+1)
miu[0] = 1
mau[0] = 1
for i in range(1,N+1):
    mau[i] = (mau[i-1]-A[i-1])*2
    miu[i] = miu[i-1]-A[i-1]

mad = [0]*(N+1)
mid = [0]*(N+1)
mad[-1] = A[-1]
mid[-1] = A[-1]
for i in range(N)[::-1]:
    mad[i] = mad[i+1]+A[i]
    mid[i] = ceil(mid[i+1],2)+A[i]


ans = 0
for i in range(N+1):
    if mad[i] < 0 or mau[i] < 0:
        print('-1')
        exit()
    if mid[i] > mau[i]:
        print('-1')
        exit()
    if miu[i] > mad[i]:
        print('-1')
        exit()
    ans += min(mad[i],mau[i])

print(ans)