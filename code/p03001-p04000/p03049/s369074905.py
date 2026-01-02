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
s = []
for i in range(N):
    s.append(list(input()))

count = 0
enda = 0
startb = 0
both = 0
for i in range(N):
    for j in range(len(s[i])-1):
        if s[i][j] == 'A' and s[i][j+1] == 'B':
            count += 1
    if s[i][-1] == 'A':
        enda += 1
    if s[i][0] == 'B':
        startb += 1
    if s[i][-1] == 'A' and s[i][0] == 'B':
        both += 1

temp = count+min(enda,startb)
if enda == startb == both and enda >= 1:
    temp -= 1
print(temp)