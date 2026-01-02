import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
n=N()
import collections
from bisect import bisect, bisect_left, bisect_right

sei=[collections.defaultdict(list) for i in range(4)]
hu=[collections.defaultdict(list) for i in range(4)]
ziku=[collections.defaultdict(list) for i in range(4)]
s={"U":0 ,"R":1,"D":2,"L":3}
for i in range(n):
    x,y,u=input().split()
    x,y=int(x),int(y)
    t=s[u]
    
    sei[t][x-y].append(x)
    hu[t][x+y].append(x)
    if t%2==1:
        ziku[t][y].append(x)
    else:
        ziku[t][x].append(y)
def f(l,x):
    for i in l[x].keys():
        l[x][i].sort()
f(ziku,2)
f(ziku,3)
INF=float("inf")
ans=INF
def solve(l,x):
    ans=INF
    for k,v in l[x].items():
        if k in l[x^2]:
            for j in v:
                tmp=bisect(l[x^2][k],j)
                if tmp!=len(l[x^2][k]):
                    ans=min(ans,(l[x^2][k][tmp]-j)*5)
    return ans

ans=min(ans,solve(ziku,0))
ans=min(ans,solve(ziku,1))
f(sei,2)
f(sei,3)
def solve2(l,x):
    ans=INF
    for k,v in l[x].items():
        if k in l[3-x]:
            for j in v:
                tmp=bisect(l[3-x][k],j)
                if tmp!=len(l[3-x][k]):
                    ans=min(ans,(l[3-x][k][tmp]-j)*10)
    return ans
ans=min(ans,solve2(sei,0))
ans=min(ans,solve2(sei,1))
def solve3(l,x):
    ans=INF
    for k,v in l[x].items():
        if k in l[x^1]:
            for j in v:
                tmp=bisect(l[x^1][k],j)
                if tmp!=len(l[x^1][k]):
                    ans=min(ans,(l[x^1][k][tmp]-j)*10)
    return ans
f(hu,0)
f(hu,3)
ans=min(ans,solve3(hu,1))
ans=min(ans,solve3(hu,2))
if ans==INF:
    print("SAFE")
else:
    print(ans)