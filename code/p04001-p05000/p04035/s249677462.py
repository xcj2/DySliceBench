import sys
import math
from collections import defaultdict

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

N,L = LI()
a = LI()

for i in range(N-1):
    if a[i]+a[i+1] >= L:
        print('Possible')
        for j in range(1,i+1):
            print(j)
        for j in range(i+2,N)[::-1]:
            print(j)
        print(i+1)
        exit()
    else:
        continue

print('Impossible')