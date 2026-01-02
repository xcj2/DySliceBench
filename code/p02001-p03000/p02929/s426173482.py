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

def fact(a,M=mod):
    ans = 1
    for i in range(2,a+1):
        ans = ans*i
        ans = ans%M
    return ans

N = I()
S = str(input())

if S[0]=='W':
    print(0)
    exit()

if S[2*N-1]=='W':
    print(0)
    exit()

d = ['L']*(2*N)

for i in range(1,2*N):
    if S[i]!=S[i-1]:
        d[i]=d[i-1]
    else:
        if d[i-1]=='L':
            d[i] = 'R'
        else:
            d[i] = 'L'

nr = 0
nl = 0
for i in range(2*N):
    if d[i]=='L':
        nl += 1
    else:
        nr += 1
if nl != nr:
    print(0)
    exit()



temp = 0
x = [0]*(2*N)
for i in range(2*N):
    if d[i]=='L':
        temp += 1
    else:
        x[i] = temp

ans = 1
rnum = 0
for i in range(2*N):
    if d[i]=='R':
        ans *= x[i]-rnum
        ans %= mod
        rnum += 1

ans *= fact(N)
ans %= mod

print(ans)