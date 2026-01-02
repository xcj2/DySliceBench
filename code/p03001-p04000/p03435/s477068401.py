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

c = []
for _ in range(3):
    c.append(III())

for j in range(2):
    if c[0][j+1]-c[0][j]==c[1][j+1]-c[1][j]==c[2][j+1]-c[2][j]:
        pass
    else:
        print('No')
        exit()

for i in range(2):
    if c[i+1][0]-c[i][0]==c[i+1][1]-c[i][1]==c[i+1][2]-c[i][2]:
        pass
    else:
        print('No')
        exit()
    
print('Yes')