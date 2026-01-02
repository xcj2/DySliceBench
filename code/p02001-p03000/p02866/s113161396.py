import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

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

N = I()
D = III()

if D[0]!=0:
    print(0)
    exit()

count = [0]*(N+1)
for i in range(N):
    count[D[i]] += 1

if count[0]>=2:
    print(0)
    exit()

for i in range(N+1)[::-1]:
    if count[-1]==0:
        count.pop()
    else:
        break

ans = 1
for i in range(1,len(count)):
    ans *= count[i-1]**count[i]
    ans %= mod

print(ans)