al=list('abcdefghijklmnopqrstuvwxyz')
#####segfunc######                                                              
def segfunc(x,y):
    return x|y

def init(init_val):
    #set_val                                                                    
    for i in range(n):
        seg[i+num-1]=1<<al.index(init_val[i])
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
    ans=0
    while res>0:
        if res%2==1:
            ans+=1
        res=res//2
    return ans

ide_ele=0
n=int(input())
num=2**(n-1).bit_length()
seg=[ide_ele]*2*num
a=list(input())
init(a)
ans=0
q=int(input())

for i in range(q):
    p=list(map(str,input().split()))
    if p[0]=='1':
        update(int(p[1])-1,1<<al.index(p[2]))
    else:
        print(query(int(p[1])-1,int(p[2])))
#for i in range(n):
    #ans=max(gcd(query(0,i),query(i+1,n)),ans)
#print(ans)
