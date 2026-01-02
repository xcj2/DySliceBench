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

A = [LI() for _ in range(3)]
N = I()
b = LIR(N,1)

c = [[False]*3 for _ in range(3)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if A[j][k] == b[i]:
                c[j][k] = True
for i in range(3):
    if c[i][0] == c[i][1] == c[i][2] == True:
        print('Yes')
        exit()
for i in range(3):
    if c[0][i] == c[1][i] == c[2][i] == True:
        print('Yes')
        exit()
if c[0][0] == c[1][1] == c[2][2] == True:
    print('Yes')
    exit()
if c[0][2] == c[1][1] == c[2][0] == True:
    print('Yes')
    exit()

print('No')