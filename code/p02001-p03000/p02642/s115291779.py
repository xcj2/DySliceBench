import math
from collections import Counter
def ip():return int(input())
def imp():return map(int,input().split())
def impstr():return map(str,input().split())
def limp():return list(map(int,input().split()))
def limpstr():return list(map(str,input().split()))

n=ip()
l=limp()
if 1 in l:
    if l.count(1)==1:print(1)
    else:print(0)
    exit()
else:
    mark=[0]*(10**6+5)
    for x in l:
        if mark[x]>=1:   #X已经出现了一次
            mark[x]=2
            continue
        mark[x]=1
        i=2
        while x*i<10**6+1:
            mark[x*i]=2
            i+=1
    ans=0
    for x in l:
        if mark[x]==1:ans+=1
    print(ans)

