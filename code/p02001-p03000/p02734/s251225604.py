import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

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

N,S = LI()
A = LI()

d = defaultdict(int)
ans = 0
for i in range(N):
    temp = defaultdict(int)
    for k,v in d.items():
        temp[k] = v
    ans += d[S-A[i]]*(N-i)
    if S == A[i]:
        ans += (i+1)*(N-i)
    ans %= mod
    d[A[i]] += i+1
    for k in range(A[i]+1,3001):
        d[k] += temp[k-A[i]]
    #print(i,ans,d)
print(ans)