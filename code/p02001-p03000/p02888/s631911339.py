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
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

from bisect import bisect_left, bisect_right

N = I()
L = III()

L.sort(reverse=True)
L2 = L[::-1]

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        p = bisect_right(L2,L[i]-L[j])
        if N-1-p-j>=0:
            ans += N-1-p-j

print(ans)