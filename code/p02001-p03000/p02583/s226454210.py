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
L = LI()

count = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if L[i]+L[j] > L[k] and L[i]+L[k] > L[j] and L[j]+L[k] > L[i]:
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    count += 1

print(count)