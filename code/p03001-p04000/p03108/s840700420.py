import sys
sys.setrecursionlimit(10**9)
from collections import Counter
from itertools import permutations, combinations,combinations_with_replacement,product
from collections import defaultdict
input = sys.stdin.readline
    
icase=0
if icase==0:
    n,m=map(int,input().split())
    a=[0]*m
    b=[0]*m
    for i in range(m):
        ai,bi=map(int,input().split())
        a[i]=ai-1
        b[i]=bi-1
elif icase==1:
    n,m=4,5
    a=[0, 2, 0, 1, 0]
    b=[1, 3, 2, 2, 3]
elif icase==2:
    n,m=6,5
    a=[1, 0, 4, 2, 3]
    b=[2, 1, 5, 3, 4]
elif icase==3:
    n,m=26,25
    a=[13, 13, 7, 1, 20, 0, 2, 3, 5, 13, 0, 0, 16, 3, 1, 15, 13, 13, 16, 9, 13, 8, 12, 6, 8]
    b=[14, 18, 25, 20, 24, 19, 13, 13, 21, 22, 14, 4, 23, 25, 10, 17, 17, 20, 20, 14, 21, 9, 22, 9, 11]
elif icase==4:
    f=open(r"C:\Users\nishi\999atcoder\q100\q087\testcase_01_in.dat")
    ll=f.readline()
    n,m=map(int,ll.split())
    a=[0]*m
    b=[0]*m
    for i in range(m):
        ll=f.readline()
        ai,bi=map(int,ll.split())
        a[i]=ai-1
        b[i]=bi-1
    f.close()

pair=[i for i in range(n)]

def root(x):
    if x==pair[x]:
        return x
    else:
        tmp=root(pair[x])
        pair[x]=tmp
        return tmp

def unite(x,y):
    x=root(x)
    y=root(y)
    if x==y:
        return
    elif x>y:
        pair[x]=y
    else:
        pair[y]=x

def q087():
    cc=[]
    c1=[1]*n
    c2=defaultdict(int)
    c2[1]=n
    c=n    
#    pair=[i for i in range(n)]
    for i in range(m-1):
#------------------------
        rta=root(a[m-i-1])
        rtb=root(b[m-i-1])
        if c1[rta]>=n or c1[rtb]>=n:
            cc.append(0)
            continue
        if rta<rtb:
            d2=c1[rta]
            d3=c1[rtb]
            c1[rta]+=c1[rtb]
            c1[rtb]=0
            d1=c1[rta]
#        pair[rtb]=rta
            unite(a[m-i-1],b[m-i-1])
        elif rta>rtb:
            d2=c1[rta]
            d3=c1[rtb]
            c1[rtb]+=c1[rta]
            c1[rta]=0
            d1=c1[rtb]
#        pair[rta]=rtb
            unite(a[m-i-1],b[m-i-1])
        else:
            cc.append(c)
            continue

        c2[d1]+=1    
        if c2[d2]>0:
            c2[d2]-=1
#    if c2[d2]==0:
#        del c2[d2]
        if c2[d3]>0:
            c2[d3]-=1
#    if c2[d3]==0:
#        del c2[d3]
#    print(c1)        
#    print(c2)     
        q=[]
        for c2k,c2v in c2.items():
            if c2v==0:
                q.append(c2k)
        while q:
            del c2[q.pop()]            
#    print(c2)     
        c3=[]
        for c2k,c2v in c2.items():
            c3.append((c2k,c2k*c2v))

        c=0
#    for i in range(len(c3)):
        for i,c3i in enumerate(c3):
            c+=c3i[1]*(c3i[1]-c3i[0])//2
#        for j in range(i+1,len(c3)):
            for j,c3j in enumerate(c3[0:i]):
                c+=c3i[1]*c3j[1]
        cc.append(c)

    for i in range(m-2,-1,-1):
        print(cc[i])
    print(n*(n-1)//2)
#-------------------------------
q087()
#-------------------------------

