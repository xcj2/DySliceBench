import math
import collections
import sys

input = sys.stdin.readline
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]

n=I()
s=input()
r=[]
g=[]
t=[]
for i in range(n):
    if s[i:i+1]=="R":
        r.append(i)
    elif s[i:i+1]=="G":
        g.append(i)
    else:
        t.append(i)
R=len(r)
G=len(g)
T=n-R-G
ans=R*G*T
for i in range(n-1):
    for j in range(i+1,n):
        if s[i]!=s[j]:
            if j<2*i-j<=n-1:
                if s[i]!=s[2*i-j] and s[j]!=s[2*i-j]:
                    ans-=1
            if j<2*j-i<=n-1:
                if s[i]!=s[2*j-i] and s[j]!=s[2*j-i]:
                    ans-=1
            if (i+j)%2==0 and j<(i+j)//2 and s[i]!=s[(i+j)//2] and s[j]!=s[(i+j)//2]:
                ans-=1
print(ans)