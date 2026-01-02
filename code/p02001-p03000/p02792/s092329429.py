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
info=[]
for i in range(1,n+1):
    if i%10!=0:
        info.append(str(i)[0]+str(i)[-1])
#print(info)
c=collections.Counter(info)
#print(c)
ans=0
for i in range(1,10):
    for j in range(1,10):
        if i==j:
            ans+=(c[str(i)+str(j)])**2
            #print(i,j,end=" ")
            #print((c[str(i)+str(j)])**2)
        else:
            ans+=(c[str(i)+str(j)])*(c[str(j)+str(i)])
            #print(i,j,end=" ")
            #print((c[str(i)+str(j)])*(c[str(j)+str(i)]))
print(ans)