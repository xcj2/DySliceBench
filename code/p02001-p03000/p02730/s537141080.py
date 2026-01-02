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

S = str(input())
n = len(S)

for i in range(n):
    if S[i] != S[n-1-i]:
        print('No')
        exit()

for i in range((n-1)//2):
    if S[i] != S[(n-3)//2-i]:
        print('No')
        exit()

for i in range((n+1)//2,n):
    if S[i] != S[(3*n-1)//2-i]:
        print('No')
        exit()

print('Yes')