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
B = III()

ans = 0
for i in range(N):
    if i==0:
        ans += B[i]
    elif i==N-1:
        ans += B[i-1]
    else:
        ans += min(B[i-1], B[i])

print(ans)