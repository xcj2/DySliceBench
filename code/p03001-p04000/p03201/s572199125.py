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

from bisect import bisect_left

N = I()
A = III()
A.sort()

val = []
num = []
before = 0
for a in A:
    if a != before:
        val.append(a)
        num.append(1)
        before = a
    else:
        num[-1] += 1

ans = 0

for i in range(N)[::-1]:
    s = math.floor(math.log(2*A[i],2))
    p = bisect_left(val,2**s-A[i])
    if A[i]==2**s-A[i]:
        if num[p]>=2:
            ans += 1
            num[p] -= 2
    else:
        j = bisect_left(val,A[i])
        if p<=len(val)-1:
            if val[p]==2**s-A[i] and num[j] and num[p]:
                ans += 1
                num[j] -= 1
                num[p] -= 1

print(ans)