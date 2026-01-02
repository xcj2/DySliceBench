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
S = str(input())

R = []
G = []
B = []

for i in range(N):
    if S[i] == 'R':
        R.append(i)
    elif S[i] == 'G':
        G.append(i)
    else:
        B.append(i)

ans = 0
for r in R:
    for g in G:
        ans += len(B)
        mi,ma = min(r,g),max(r,g)
        p = bisect_left(B,2*ma-mi)
        if 0<= p <= len(B)-1 and B[p] == 2*ma-mi and 2*ma-mi > ma:
            ans -= 1
        p = bisect_left(B,(ma+mi)/2)
        if 0<= p <= len(B)-1 and B[p] == (ma+mi)/2 and mi<B[p]<ma:
            ans -= 1
        p = bisect_left(B,2*mi-ma)
        if 0 <= p <= len(B)-1 and B[p] == 2*mi-ma and B[p]<mi:
            ans -= 1
print(ans)