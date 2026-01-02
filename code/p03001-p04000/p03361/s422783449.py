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

from itertools import product

H,W = II()
s = [list(map(str, input())) for _ in range(H)]

def neighbor(i,j):
    if H==1:
        x = []
    else:
        if i==0:
            x = [1]
        elif i==H-1:
            x = [H-2]
        else:
            x = [i-1,i+1]
    if W==1:
        y = []
    else:
        if j==0:
            y = [1]
        elif j==W-1:
            y = [W-2]
        else:
            y = [j-1,j+1]
    return  list(product(x,[j])) + list(product([i],y))  

for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            flag = True
            a = neighbor(i,j)
            for k in a:
                if s[k[0]][k[1]] == '#':
                    flag = False
                    break
            if flag:
                print('No')
                exit()

print('Yes')