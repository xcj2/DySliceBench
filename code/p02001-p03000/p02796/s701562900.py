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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()
X,L = Line(N,2)

from operator import itemgetter
def index_sort(A):
    return sorted(enumerate(A),key=itemgetter(1))

B = [X[i]+L[i] for i in range(N)]
C = index_sort(B)
X = [X[c[0]] for c in C]
L = [L[c[0]] for c in C]

count = 0
right = -float('inf')
for i in range(N):
    now = X[i]-L[i]
    if now>=right:
        count += 1
        right = X[i]+L[i]
    else:
        continue

print(count)