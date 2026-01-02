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

from operator import itemgetter
def index_sort(A):
    x = []
    for i,a in enumerate(A):
        x.append((a,i))
    return sorted(x, key=itemgetter(0),reverse=True)

n = I()
a = III()

A = index_sort(a)
amax = A[0][0]
index = A[0][1]

temp = float('inf')
for i in range(n):
    if i==index:
        continue
    if abs(amax/2 - a[i])<abs(amax/2 - temp):
        temp = a[i]

print(amax,temp)