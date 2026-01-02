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
memo = [{} for _ in range(N+1)]

def ok(last4):
    for i in range(4):
        s = list(last4)
        if i>=1:
            s[i-1], s[i] = s[i], s[i-1]
        if 'AGC' in ''.join(s):
            return False
    return True

def rec(cur, s):
    if s in memo[cur]:
        return memo[cur][s]
    if cur==N:
        return 1
    ret = 0
    for c in 'AGCT':
        if ok(s+c):
            ret = (ret + rec(cur+1, s[-2:]+c))%mod
    memo[cur][s] = ret
    return ret

print(rec(0,'TTT'))