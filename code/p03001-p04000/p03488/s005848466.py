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

s = str(input())
x,y = II()

N = len(s)
yoko = []
tate = []
ziku = True
count = 0

for i in range(N):
    if s[i]=='F':
        count += 1
    else:
        if ziku:
            yoko.append(count)
            ziku = False
        else:
            tate.append(count)
            ziku = True
        count = 0

if count!=0:
    if ziku:
        yoko.append(count)
    else:
        tate.append(count)

yoko.append(0)
tate.append(0)

if s[0]=='F':
    fstart = True
else:
    fstart = False

sum1 = sum(yoko)
sum2 = sum(tate)

if abs(x)>sum1 or abs(y)>sum2:
    print('No')
    exit()

yoko_yes = [False]*(2*sum1+1)
yoko_yes[sum1] = True

for k,yk in enumerate(yoko):
    ok = []
    if k==0 and fstart:
        ok.append(sum1+yk)
    else:
        for i in range(2*sum1+1):
            if yoko_yes[i]:
                if 0<=i+yk<=2*sum1:
                    ok.append(i+yk)
                if 0<=i-yk<=2*sum1:
                    ok.append(i-yk)
    yoko_yes = [False]*(2*sum1+1)
    for o in ok:
        yoko_yes[o] = True

tate_yes = [False]*(2*sum2+1)
tate_yes[sum2] = True

for t in tate:
    ok = []
    for i in range(2*sum2+1):
        if tate_yes[i]:
            if 0<=i+t<=2*sum2:
                ok.append(i+t)
            if 0<=i-t<=2*sum2:
                ok.append(i-t)
    tate_yes = [False]*(2*sum2+1)
    for o in ok:
        tate_yes[o] = True

if yoko_yes[x+sum1] and tate_yes[y+sum2]:
    print('Yes')
else:
    print('No')