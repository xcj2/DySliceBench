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

N = I()

def dfs(s):
    if int(s)>N:
        return 0
    else:
        if all(s.count(c)>=1 for c in ['3','5','7']):
            ret = 1
        else:
            ret = 0
        for x in ['3','5','7']:
            ret += dfs(s+x)
        return ret

print(dfs('0'))