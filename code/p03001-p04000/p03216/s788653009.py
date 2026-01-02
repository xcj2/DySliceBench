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
S = list(input())
Q = I()
k = LI()

cumD = [0]*N
cumM = [0]*N
cumDM = [0]*N

cumD[0] = 1 if S[0] == 'D' else 0
cumM[0] = 1 if S[0] == 'M' else 0

Clist = []
for i in range(1,N):
    cumD[i] = cumD[i-1]
    cumM[i] = cumM[i-1]
    cumDM[i] = cumDM[i-1]
    if S[i] == 'D':
        cumD[i] += 1
        continue
    if S[i] == 'M':
        cumM[i] += 1
        cumDM[i] += cumD[i-1]
        continue
    if S[i] == 'C':
        Clist.append(i)

for j in range(Q):
    ans = 0
    for i in Clist:
        if i-k[j] >= 0:
            ans += cumDM[i-1] - (cumD[i-k[j]])*(cumM[i-1]-cumM[i-k[j]]) - cumDM[i-k[j]]
        else:
            ans += cumDM[i-1]
    print(ans)