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

N,K = II()
x = [0]*N
y = [0]*N
z = ['0']*N
for i in range(N):
    a,b,c = input().split()
    x[i],y[i],z[i] = int(a),int(b),c

x,y = y,x

for i in range(N):
    if z[i]=='B':
        x[i] = (2*K-1)-x[i]%(2*K)
        y[i] = y[i]%(2*K)
    else:
        x[i] += K
        x[i] = (2*K-1)-x[i]%(2*K)
        y[i] = y[i]%(2*K)

kukan = []
for i in range(N):
    if x[i]+K-1<=2*K-1:
        if y[i]-K+1>=0:
            kukan.append([x[i],x[i]+K-1,y[i]-K+1,y[i]])
        else:
            kukan.append([x[i],x[i]+K-1,0,y[i]])
            kukan.append([x[i],x[i]+K-1,K+y[i]+1,2*K-1])
    else:
        if y[i]-K+1>=0:
            kukan.append([0,x[i]-K-1,y[i]-K+1,y[i]])
            kukan.append([x[i],2*K-1,y[i]-K+1,y[i]])
        else:
            kukan.append([0,x[i]-K-1,0,y[i]])
            kukan.append([0,x[i]-K-1,K+y[i]+1,2*K-1])
            kukan.append([x[i],2*K-1,0,y[i]])
            kukan.append([x[i],2*K-1,K+y[i]+1,2*K-1])

tiles = [[0]*(2*K+1) for _ in range(2*K+1)]
for k in kukan:
    tiles[k[0]][k[2]] += 1
    tiles[k[0]][k[3]+1] -= 1
    tiles[k[1]+1][k[2]] -= 1
    tiles[k[1]+1][k[3]+1] += 1

for i in range(2*K):
    for j in range(1,2*K):
        tiles[i][j] += tiles[i][j-1]

for i in range(1,2*K):
    for j in range(2*K):
        tiles[i][j] += tiles[i-1][j]

ans = 0
for i in range(2*K):
    for j in range(2*K):
        if tiles[i][j]+tiles[(i+K)%(2*K)][(j+K)%(2*K)]>ans:
            ans = tiles[i][j]+tiles[(i+K)%(2*K)][(j+K)%(2*K)]

print(ans)