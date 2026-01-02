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

N = I()
L,R = Line(N,2)

l = max(L)
li = L.index(l)
r = min(R)
ri = R.index(r)
ans = max(r-l+1,0) + max([0 if (i==li or i==ri) else R[i]-L[i]+1 for i in range(N)])
if li==ri:
    print(ans)
    exit()

x = []
for i in range(N):
    if i==li or i==ri:
        continue
    else:
        x1 = max(R[i]-l+1, 0)
        x2 = max(r-L[i]+1, 0)
        x.append((x1,x2))

x.sort(key=lambda s:(-s[0],s[1]))

amin = R[li]-l+1
bmin = r-L[ri]+1
one = [amin]
two = [bmin]

for x0 in x:
    amin = min(amin,x0[0])
    one.append(amin)
for x0 in x[::-1]:
    bmin = min(bmin,x0[1])
    two.append(bmin)

two = list(reversed(two))
for i in range(len(one)):
    temp = one[i]+two[i]
    if temp>ans:
        ans = temp

print(ans)