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

N = I()
S = []
for _ in range(N):
    S.append(str(input()))

ans = 0
for b in range(N):
    flag = True
    for i in range(N):
        for j in range(i+1,N):
            if S[i][(j+b)%N] != S[j][(i+b)%N]:
                flag = False
                break
        else:
            continue
        break
    if flag:
        ans += N

print(ans)