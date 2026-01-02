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

N,K,C = LI()
S = str(input())

L = []
R = []

for i in range(N):
    if S[i] == 'o':
        if len(L) == 0:
            L.append(i)
        else:
            if L[-1]+C+1 <= i:
                L.append(i)
    if len(L) == K:
        break

for i in range(N)[::-1]:
    if S[i] == 'o':
        if len(R) == 0:
            R.append(i)
        else:
            if R[-1]-C-1 >= i:
                R.append(i)
    if len(R) == K:
        break

R = list(reversed(R))

for i in range(len(L)):
    if L[i] == R[i]:
        print(L[i]+1)