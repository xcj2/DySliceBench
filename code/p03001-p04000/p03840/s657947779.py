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

# T,S,Zは使えない
# I,J,Lを1つずつ使うと偶奇の調整ができる

A = LI()
d = defaultdict()
name = ['I','O','T','J','L','S','Z']
for i,a in enumerate(A):
    d[name[i]] = a

ans = d['O']

use = ['I','J','L']
odd = []
even = []
for k in use:
    if d[k]%2:
        odd.append(k)
    else:
        even.append(k)

if len(odd) == 3:
    ans += 3
    for k in use:
        ans += ((d[k]-1)//2)*2
elif len(odd) == 2:
    if d[even[0]] > 0:
        ans += 3
        for k in use:
            ans += ((d[k]-1)//2)*2
    else:
        for k in use:
            ans += (d[k]//2)*2
elif len(odd) == 1:
    for k in use:
        ans += (d[k]//2)*2
else:
    for k in use:
        ans += (d[k]//2)*2

print(ans)