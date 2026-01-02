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
H = III()

ans = 0
temp = 0
for i in range(1,N)[::-1]:
    if H[i] <= H[i-1]:
        temp += 1
    else:
        if ans < temp:
            ans = temp
        temp = 0

print(max(ans,temp))