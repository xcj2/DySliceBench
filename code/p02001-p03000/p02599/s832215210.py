import sys
input=sys.stdin.readline
#####segfunc######                                                              
def segfunc(x,y):
    return x+y

def init(init_val):
    #set_val                                                                    
    for i in range(n):
        seg[i+num-1]=init_val[i]
    #built                                                                      
    for i in range(num-2,-1,-1):
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2])
    
def update(k,x):
    k+=num-1
    seg[k]=x
    while k+1:
        k=(k-1)//2
        seg[k]=segfunc(seg[k*2+1],seg[k*2+2])

def query(p,q):
    if q<=p:
        return ide_ele
    p+=num-1
    q+=num-2
    res=ide_ele
    while q-p>1:
        if p&1==0:
            res=segfunc(res,seg[p])
        if q&1==1:
            res=segfunc(res,seg[q])
            q-=1
        p=p//2
        q=(q-1)//2
    if p==q:
        res=segfunc(res,seg[p])
    else:
        res=segfunc(segfunc(res,seg[p]),seg[q])
    return res

ide_ele=0
n,q=map(int,input().split())
num=2**(n-1).bit_length()
seg=[ide_ele]*2*num
c=list(map(int,input().split()))
lr=[]
for i in range(q):
    lr.append(list(map(int,input().split())) + [i])
lr.sort(key=lambda x: x[1])
ans=[0]*q
ll=0
lastc=[-1]*(n+1)
for l,r,ind in lr:
    l-=1
    r-=1
    while ll<=r:
        if lastc[c[ll]]==-1:
            lastc[c[ll]]=ll
            update(ll,1)
        else:
            update(lastc[c[ll]],0)
            lastc[c[ll]]=ll
            update(lastc[c[ll]],1)
        ll+=1
    ans[ind]=query(l,r+1)
for i in ans:
    print(i)
