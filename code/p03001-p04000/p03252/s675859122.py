#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

S = list(str(input()))
T = list(str(input()))

a = defaultdict()

for i in range(len(S)):
    if S[i] in a.keys():
        if a[S[i]]==T[i]:
            continue
        else:
            print('No')
            exit()
    else:
        if T[i] in a.values():
            print('No')
            exit()
        else:
            a[S[i]] = T[i]
                      
print('Yes')