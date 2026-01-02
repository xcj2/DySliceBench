def halfsplitsearch(list,start,end,minmax):
    if minmax=='min':
        while end-start>1:
            test=(end+start)//2
            if condition(list[test][0]):
                end=test
            else:
                start=test
        if condition(list[start][0]):
            return start
        else:
            return end
    else:
        while end-start>1:
            test=(end+start)//2
            if condition(list[test][0]):
                start=test
            else:
                end=test
        if condition(list[end][0]):
            return end
        else:
            return start

import sys

input=sys.stdin.readline

A,B,Q=map(int,input().split())
s=[[] for i in range(0,A)]
for i in range(0,A):
    y=int(input())
    s[i]=[y,'s',i]
t=[[] for i in range(0,B)]
for i in range(0,B):
    y=int(input())
    t[i]=[y,'t',i]
x=[0 for i in range(0,Q)]
for i in range(0,Q):
    x[i]=int(input())

list=s+t
list.sort()
s.sort()
t.sort()

sans=[0 for i in range(0,A)]
for i in range(0,A):
    ans=0
    def condition(num):
        return num<s[i][0]
    ans=halfsplitsearch(t,0,len(t)-1,'max')
    if ans!=B-1:
        sans[i]=min(abs(s[i][0]-t[ans][0]),abs(s[i][0]-t[ans+1][0]))
    else:
        sans[i]=abs(s[i][0]-t[ans][0])

tans=[0 for i in range(0,B)]
for i in range(0,B):
    ans=0
    def condition(num):
        return num<t[i][0]
    ans=halfsplitsearch(s,0,len(s)-1,'max')
    if ans!=A-1:
        tans[i]=min(abs(t[i][0]-s[ans][0]),abs(t[i][0]-s[ans+1][0]))
    else:
        tans[i]=abs(t[i][0]-s[ans][0])


for i in range(0,Q):
    a=0
    b=0
    test1=10**100
    test2=10**100
    def condition(num):
        return num<x[i]
    a=halfsplitsearch(list,0,len(list)-1,'max')
    if list[a][1]=='s':
        test1=abs(x[i]-list[a][0])+sans[list[a][2]]
    else:
        test1=abs(x[i]-list[a][0])+tans[list[a][2]]
    if a!=len(list)-1:
        if list[a+1][1]=='s':
            test2=abs(x[i]-list[a+1][0])+sans[list[a+1][2]]
        else:
            test2=abs(x[i]-list[a+1][0])+tans[list[a+1][2]]
    print(min(test1,test2))