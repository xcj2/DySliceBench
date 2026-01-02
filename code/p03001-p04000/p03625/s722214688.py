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

N = I()
A = III()

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

A = list(set(A))
A.sort(reverse=True)

l1 = 0
l2 = 0
for a in A:
    if d[a]>=2:
        if l1==0:
            l1 = a
        else:
            l2 = a
            break
        d[a] -= 2
        if d[a]>=2:
            l2 = a
            break
    else:
        continue

print(l1*l2)