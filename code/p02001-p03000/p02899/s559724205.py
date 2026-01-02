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

from operator import itemgetter
def index_sort(A):
    return sorted(enumerate(A),key=itemgetter(1))

N = I()
A = III()

x = index_sort(A)
y = []
for i in range(N):
    y.append(x[i][0]+1)

print(*y)