import bisect
n=int(input())
x=[]
d=[]
mod=998244353
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort(key=lambda x:x[0])
for i in range(n):
    a,b=l[i][0],l[i][1]
    x.append(a)
    d.append(b)

r=[0]*n
r[-1]=n-1
for i in range(n-2,-1,-1):
    xi=bisect.bisect_left(x,x[i]+d[i])
    xi-=1
    r[i]=xi
    #if xi==i:
        #r[i]=i
    #else:
        #r[i]=r[xi]

#####segfunc######                                                              
def segfunc(x,y):
    return max(x,y)

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

ide_ele=-10
num=2**(n-1).bit_length()
seg=[ide_ele]*2*num
init(r)
rr=[0]*n
rr[-1]=n-1
for i in range(n-2,-1,-1):
    rr[i]=query(i,r[i]+1)
    update(i,rr[i])

dp=[0]*(n+1)
dp[-2]=2
dp[-1]=1
for i in range(n-2,-1,-1):    
    dp[i]=(dp[i+1]+dp[rr[i]+1])%mod
print((dp[0])%mod)