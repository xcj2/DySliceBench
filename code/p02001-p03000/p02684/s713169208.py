from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())


    
n,m=mi()
a=li()
x=[]
c=1
k=0
m1={}
m1[1]=k
k+=1
x1=0
while(1):
    if a[c-1] in m1:
        x1=a[c-1]
        break
    m1[a[c-1]]=k
    k+=1
    c=a[c-1]
if(m<k):
    for i in m1.keys():
        if m1[i]==m:
            print(i)
            break
else:
    m-=k
    m1={}
    m1[x1]=0
    k=1
    c=a[c-1]
    while(1):
        if a[c-1] in m1:
            break
        m1[a[c-1]]=k
        k+=1
        c=a[c-1]
    m%=k
    for i in m1.keys():
        if m1[i]==m:
            print(i)
            break
    
    
    
    
    