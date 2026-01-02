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
a = III()

count = [0]*(10**5+1)
for i in range(N):
    count[a[i]] += 1

ans = 0
for i in range(1,10**5):
    temp = count[i]+count[i-1]+count[i+1]
    if temp>ans:
        ans = temp

print(ans)