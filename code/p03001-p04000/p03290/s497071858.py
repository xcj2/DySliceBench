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

D,G = II()
p,c = Line(D)

def dfs(point,p):
    if point<=0:
        return 0
    else:
        ret = []
        for i in range(D):
            if p[i]==0:
                continue
            q,mod = divmod(point,(i+1)*100)
            if mod ==0:
                num = q
            else:
                num = q+1
            if num <= p[i]:
                ret.append(num)
            else:
                temp = p[i]
                p[i] = 0
                ret.append(dfs(point-100*(i+1)*temp-c[i],p)+temp)
                p[i] = temp
        return min(ret)

print(dfs(G,p))