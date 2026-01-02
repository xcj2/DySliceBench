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

S = str(input())
n = len(S)
K = I()

for i in range(1,n):
    if S[i]!=S[i-1]:
        break
    else:
        if i==n-1:
            print(K*n//2)
            exit()

if n==1:
    print(K//2)
    exit()

ren = 1
num = 0
for i in range(1,n):
    if S[i]==S[i-1]:
        ren += 1
    else:
        if i!=n-1:
            num += ren//2
            ren = 1

last = ren

if S[0]==S[-1]:
    num2 = 0
    for i in range(n):
        if S[i]==S[-1]:
            ren += 1
        else:
            now = i
            break
    num2 += ren//2
    ren = 1
    for i in range(now,n):
        if S[i]==S[i-1]:
            ren += 1
        else:
            if i!=n-1:
                num2 += ren//2
                ren = 1
    num3 = 0
    ren = 1
    for i in range(n-1-last+2,n):
        if S[i]==S[i-1]:
            ren += 1
        else:
            num3 += ren//2
            ren = 1
    num3 += ren//2
    print(num+num2*(K-1)+num3)
else:
    num += ren//2
    print(num*K)