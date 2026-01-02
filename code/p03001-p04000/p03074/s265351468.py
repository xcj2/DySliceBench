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

N,K = II()
S = str(input())

num = 0
for i in range(N):
    if i==N-1:
        print(N)
        exit()
    if S[i]=='0' and S[i+1]=='1':
        num += 1
        place = i+1
    if num==K:
        break

if num<K:
    print(N)
    exit()

for i in range(place+1,N):
    if i==N-1 and S[i]=='1':
        print(N)
        exit()
    if S[i]=='0':
        break

place = i-1

ans = place+1

for i in range(1,N):
    if S[i-1]=='0' and S[i]=='1':
        val = N-1
        for j in range(place+2,N):
            val = j
            if j==N-1:
                break
            if S[j]=='1' and S[j+1]=='0':
                break
        if val-i+1>ans:
            ans = val-i+1
        place = val

print(ans)