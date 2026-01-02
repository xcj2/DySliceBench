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
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N,C = II()
x,v = Line(N)

#時計のみ
ans1 = 0
a = []
for i in range(N):
    a.append([x[i],v[i]])
a2 = sorted(a,key=lambda x:x[0])
temp = 0
for i in range(N):
    temp += a2[i][1]
    if temp-a2[i][0]>ans1:
        ans1 = temp-a2[i][0]

#反時計のみ
ans2 = 0
temp = 0
for i in range(N)[::-1]:
    temp += a2[i][1]
    if temp-(C-a2[i][0])>ans2:
        ans2 = temp-(C-a2[i][0])

ans = max(ans1,ans2)

#時計>=反時計
b = [] #反時計向きの個数,得
temp = 0
for i in range(N)[::-1]:
    temp += a[i][1]
    b.append([N-i,temp-2*(C-a[i][0])])
b.sort(key=lambda x:-x[1])
now = 0
a_temp = 0
for i in range(N):
    a_temp += a[i][1]
    while now<=N-1:
        if b[now][0]+i+1>N:
            now += 1
        else:
            temp = b[now][1]+a_temp-a[i][0]
            if temp>ans:
                ans = temp
            break

#時計<反時計
b = [] #時計向きの個数,得
temp = 0
for i in range(N):
    temp += a[i][1]
    b.append([i+1,temp-2*a[i][0]])
b.sort(key=lambda x:-x[1])
now = 0
a_temp = 0
for i in range(N)[::-1]:
    a_temp += a[i][1]
    while now<=N-1:
        if b[now][0]+N-i>N:
            now += 1
        else:
            temp = b[now][1]+a_temp-(C-a[i][0])
            if temp>ans:
                ans = temp
            break

print(ans)