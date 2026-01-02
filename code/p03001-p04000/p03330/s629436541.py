import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N,C = II()
D = []
for i in range(C):
    D.append(III())
c = []
for i in range(N):
    c.append(III())

d1 = []
d2 = []
d3 = []
for i in range(N):
    for j in range(N):
        if (i+j)%3==0:
            d1.append(c[i][j])
        elif (i+j)%3==1:
            d2.append(c[i][j])
        else:
            d3.append(c[i][j])

d1val = []
d2val = []
d3val = []

for cl in range(C):
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for dcl in d1:
        temp1 += D[dcl-1][cl]
    for dcl in d2:
        temp2 += D[dcl-1][cl]
    for dcl in d3:
        temp3 += D[dcl-1][cl]
    d1val.append(temp1)
    d2val.append(temp2)
    d3val.append(temp3)

ans = float('inf')
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i==j or i==k or j==k:
                continue
            else:
                temp = d1val[i]+d2val[j]+d3val[k]
                if temp<ans:
                    ans = temp

print(ans)