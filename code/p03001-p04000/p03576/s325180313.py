import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(N,num):
    if N<=0:
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [LI() for _ in range(N)]
        return map(list, zip(*read_all))

#################

from bisect import bisect_left
from itertools import product,combinations

from operator import itemgetter
def index_sort(A):
    A_sort = sorted(enumerate(A),key=itemgetter(1))
    index = [a[0] for a in A_sort]
    sorted_A = [a[1] for a in A_sort]
    return index, sorted_A

N,K = LI()
x,y = MI(N,2)

index,_ = index_sort(x)
x2 = [x[i] for i in index]
y2 = [y[i] for i in index]

A = list(product(combinations(range(N),2),repeat=2))
ans = float('inf')
for a in A:
    xmin = min(x[a[0][0]],x[a[0][1]])
    xmax = max(x[a[0][0]],x[a[0][1]])
    ymin = min(y[a[1][0]],y[a[1][1]])
    ymax = max(y[a[1][0]],y[a[1][1]])
    S = (xmax-xmin)*(ymax-ymin)
    if S >= ans:
        continue
    l = bisect_left(x2,xmin)
    r = bisect_left(x2,xmax)
    num = 0
    for i in range(l,r+1):
        if ymin <= y2[i] <= ymax:
            num += 1
    if num >= K:
        ans = S

print(ans)