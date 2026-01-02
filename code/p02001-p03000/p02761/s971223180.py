import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N,M = LI()
s,c = LIR(M,2)

if M==0:
    if N==1:
        print(0)
    elif N==2:
        print(10)
    else:
        print(100)
    exit()


x = [-1]*N
for i in range(M):
    if x[s[i]-1]!=-1 and x[s[i]-1]!=c[i]:
        print(-1)
        exit()
    else:
        x[s[i]-1]=c[i]

if x[0]==0:
    if N==1:
        print(0)
        exit()
    else:
        print(-1)
        exit()

for i in range(N):
    if x[i]==-1:
        if i==0:
            x[i] = 1
        else:
            x[i] = 0

y = ''
for i in range(N):
    y += str(x[i])

print(int(y))