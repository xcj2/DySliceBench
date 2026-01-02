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
A = [I() for _ in range(N)]

d = defaultdict(int)
for i in range(N):
    if d[A[i]]==0:
        d[A[i]] = 1
    else:
        d[A[i]] = 0

ans = 0
for k in d.keys():
    if d[k] != 0:
        ans += 1
        
print(ans)