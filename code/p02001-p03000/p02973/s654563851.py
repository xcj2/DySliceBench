from heapq import heappush, heappop
from collections import deque
import sys
#import bisect
sys.setrecursionlimit(10**6)
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]

def bisect(ls,x):
    l,r=0,len(ls)
    while r-l>1:
        mid=(l+r)//2
        if ls[mid]>=x: # condition
            r=mid
        else:
            l=mid
    #print('bisect',ls,x,'=',r)
    return l

n=I()
a=deque()
q=[[] for _ in range(n)]
m=0 # num of queue now
for i in range(n):
    a+=[I()]
#print('a=',a)

q=deque()
q.append(a.popleft())
#print(q,'q[',0,']=')

while a:
    c=a.popleft()
    if c<=q[0]:
        q.appendleft(c)
        #print(q,'q[',0,']=',c)
    else:
        i=bisect(q,c)
        q[i]=c
        #print(q,'q[',i,']=',c)


ans=len(q)
print(ans)
