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

ide_ele=0
n=int(input())
num=2**(n-1).bit_length()
seg=[ide_ele]*2*num
h=list(map(int,input().split()))
a=list(map(int,input().split()))
dp=[0]*n
init(dp)
ans=0
for i in range(n):
    tmp=query(0,h[i])
    update(h[i]-1,tmp+a[i])

ans=query(0,n)
print(ans)
